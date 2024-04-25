print("Config package initialized.")

DEBUG = True

# MODEL -----------------------------------------------------------------------
USE_MODEL = 'GLM'  # 「chatGPT， Qwen， GLM」

# OpenAI https://api.openai.com/v1/chat/completions
GPT_URL = 'https://api.openai.com/v1/chat/completions'
GPT_API_KEY = 'sk-xxxxxx'

# GLM-4 https://open.bigmodel.cn/api/paas/v4/chat/completions
GLM4_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
GLM4_API_KEY = 'sk-xxxxxx'

# Qwen
Qwen_URL = 'https://www.your-local-Qwenurl/'


# MODEL ------------------------------------------------------------------------

# CONFIGURATION ----------------------------------------------------------------

# 意图相关性判断阈值0～1
RELATED_INTENT_THRESHOLD = 0.5

# CONFIGURATION ----------------------------------------------------------------
