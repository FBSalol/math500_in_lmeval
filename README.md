# math500_in_lmeval
`compare.md`文件内为主流模型在 **Math-500** 上的公开评测分数。

`math500/`文件夹内为 **lm-evaluation-harness** 框架下实现 **Math-500** 数据集的相关文件。


## 环境配置
使用**lm-evaluation-harness**框架下的环境，再下载**pylatexenc**包即可：

```bash
pip install pylatexenc
```

## 运行实例
将`math500/`文件夹放在 **lm-evaluation-harness** 框架下`lm-evaluation-harness-main/lm_eval/tasks/`内。

```bash
lm_eval --tasks math500 --model hf --batch_size 8 --model_args pretrained=deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --output_path results
```

## 日志文件
官方公布的 **DeepSeek-R1-Distill-Qwen-1.5B** 模型在数据集 **Math-500** 上的测试结果为 **83.9**。

本地测试最好结果为 **9.6**。

`log/`文件夹内为结果分别为9和9.6的输出和日志文件。

`test/`文件夹内为一些测试日志。

## 分析文档
在`analyze/`文件夹下。
