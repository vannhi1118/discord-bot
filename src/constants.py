from enum import Enum

# Enum for error codes
class ErrorCode(Enum):
    USED_WORD = 0
    LAST_USER = 1
    INVALID_WORD = 2
    NON_EXISTENT_WORD = 3

# Dictionary to map error codes to error strings
ERROR_STRINGS = {
    ErrorCode.USED_WORD: "❌ Từ đó đã được sử dụng!",
    ErrorCode.INVALID_WORD: "❌ Từ của bạn phải bắt đầu với `{}`.",
    ErrorCode.LAST_USER: "❌ Chưa đến lượt của `{}`.",
    ErrorCode.NON_EXISTENT_WORD: "❌ Từ `{}` không tồn tại trong từ điển."
}

WORDTRAIN_COMMANDS = [
    "starttrain",
    "stoptrain",
    "wordtrain"
]

WORDTRAIN_STRINGS = {
    "start": "🚂 Word Train đã bắt đầu! Ai cũng có thể nói một từ để bắt đầu!",
    "stop": "🛑 Word Train đã dừng lại.",
    "no_train": "Không có chuyến tàu nào đang chạy trong kênh này.",
    "unknown_error": "❓ Đã xảy ra lỗi không xác định. Vui lòng thử lại.",
    "game_end": "🚂 Chuyến tàu đã kết thúc với từ `{}`!",
}