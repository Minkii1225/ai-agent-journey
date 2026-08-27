# DeepSeek API 请求结构测试记录

> W6 周二产物 | 测试工具：Apifox | 模型：deepseek-v4-pro

## 一、测试目标

用 Apifox 手动调用 DeepSeek 对话接口，搞清楚一个 HTTP 请求由哪几部分组成，以及不同参数对输出的影响。

## 二、请求结构

- **URL**: https://api.deepseek.com/chat/completions
- **Method**: POST
- **Headers**:

| Header | 值 | 作用 |
|--------|-----|------|
| Content-Type | application/json | 告诉服务器我发的是 JSON 格式数据 |
| Authorization | Bearer sk-****69ea | 身份认证（Key 已打码，只留末 4 位） |

- **Body**:

```json
{
    "model": "deepseek-v4-pro",
    "messages": [
        {"role": "user", "content": "给一个咖啡店起名字，只说一个"}
    ],
    "temperature": 0
}
```

注意层级：`model` / `messages` / `temperature` 是**平级**参数，都在最外层大括号里。

## 三、响应结构

我关注的关键字段：

| 字段 | 我的理解 |
|------|---------|
| choices[0].message.content | 模型最终回复内容（程序里要取的就是它） |
| choices[0].message.reasoning_content | 模型的思考过程（deepseek-v4-pro 是推理模型，先想后答） |
| choices[0].finish_reason | 结束原因：stop=正常结束，以后还会遇到 length（被截断）、tool_calls（要调工具） |
| id | 本次请求的唯一编号，可用来验证是否真的是两次不同请求 |
| created | 请求时间戳 |
| usage.total_tokens | 本次消耗的总 token 数 |
| usage.completion_tokens_details.reasoning_tokens | 花在"思考"上的 token（注意：这部分也计费） |

## 四、踩坑记录

### 1. JSON 少了最外层大括号 → 400

Body 忘了写最外层 `{}`，服务器解析失败直接返回 400。
→ JSON 对标点极其严格，一个括号都不能少。这也是为什么实际开发都用代码构造 dict 再序列化，手动拼 JSON 只适合第一次理解结构。

### 2. Key 改错一位 → 401

```json
{
    "error": {
        "message": "Authentication Fails, Your api key: ****69ea is invalid",
        "type": "authentication_error"
    }
}
```

→ 学到两点：① 看报错先看 `type` 字段分类，再读 `message` 拿细节；② 报错信息里 Key 只露末 4 位 `****69ea`，这就是打码规范——自己写文档时也应这样处理。

### 3. temperature 写进了 messages 数组 → 400

```json
{
    "error": {
        "message": "Failed to deserialize the JSON body into the target type: messages[2]: invalid type: string \"temperature\", expected internally tagged enum ChatCompletionRequestMessage at line 6 column 21",
        "type": "invalid_request_error"
    }
}
```

把 `temperature` 写到了 `messages` 数组里面，服务器以为它是第 3 条消息。
→ 报错的 `line 6 column 21` 能直接定位问题位置，读报错要读到这种精度；参数层级错了语法检查不出来，只有服务器能发现。

### 4. temperature 0 vs 1.5 对比（问题：给咖啡店起名）

| 对比项 | temperature: 0 | temperature: 1.5 |
|--------|---------------|------------------|
| 答案 | 半日闲 | 豆留 |
| 思考候选数 | 反复权衡七八个候选 | 候选少而集中 |
| reasoning_tokens | 305 | 135 |
| 响应 id | 0b0ae632-... | c6eac1b5-...（不同，确认是两次真实请求） |

有趣发现：temperature 0 反而"想得更多"——确定性路径每步都选概率最高的词，推理链容易绕圈；1.5 有随机性，反而更快锁定。
→ temperature 控制"选词的随机程度"：开放性任务（起名、创意）调高更多样，要稳定输出的任务（分类、抽取）设 0。

### 5. 第一次对比测试白测了

两次响应的 `id` 和 `created` 完全相同——复制的是同一份响应，不是两次真实请求。
→ 验证测试有效性，先比对响应 id 是否不同。

## 五、HTTP 状态码小笔记

| 状态码 | 含义 | 什么时候遇到 |
|--------|------|-------------|
| 200 | 成功 | 正常响应 |
| 400 | 请求本身有问题（格式错） | JSON 少括号 / 参数层级错 |
| 401 | 认证失败 | Key 错 / 没加 Bearer 前缀 |
| 429 | 请求太频繁（限流） | 短时间发太多请求 |
| 500 | 服务器自己出问题 | 重试即可 |

## 六、一句话总结

调一次大模型 API，本质上是发一个**带认证头、Body 为 JSON** 的 POST 请求，模型回复藏在响应的 `choices[0].message.content` 里，思考过程在 `reasoning_content` 里，花了多少钱看 `usage`。
