# 导入必要的库
from moviepy.editor import VideoFileClip
import os
import re

# 步骤1：从视频中提取帧并创建GIF
def extract_frames_and_make_gif(video_path, gif_path, start_time, end_time, fps=1):
    # 加载视频并选择开始时间和结束时间之间的子剪辑
    clip = VideoFileClip(video_path).subclip(start_time, end_time)
    # 将选定的帧写入GIF文件
    clip.write_gif(gif_path, fps=fps)

# 步骤2：使用关键词对GIF进行索引（这里，我们简单地使用文件名作为关键词）
def index_gif_with_keyword(gif_path, keyword):
    # 假设我们使用一个字典来存储从关键词到GIF路径的映射
    gif_index = {}
    gif_index[keyword] = gif_path
    return gif_index

# 步骤3：存储GIF和关键词之间的映射
# 这里，我们直接使用上面的字典，但在实际应用中，可能需要持久性存储，例如数据库
# 步骤4：实现用户评论中的关键词检测
def detect_keywords_in_comment(comment, gif_index):
    # 将评论分割成单词
    words = comment.split()
    # 检查每个单词是否在gif_index中
    for word in words:
        if word in gif_index:
            # 如果找到关键词，返回相应的GIF路径
            return gif_index[word]
    # 如果没有找到关键词，返回None
    return None

# 步骤5：根据检测到的关键词显示相应的GIF
def display_gif_for_comment(comment, gif_index):
    # 在评论中检测关键词
    gif_path = detect_keywords_in_comment(comment, gif_index)
    if gif_path:
        # 如果找到GIF路径，显示GIF
        # 例如，使用IPython.display进行显示
        from IPython.display import Image
        return Image(filename=gif_path)
    else:
        print("未找到相关GIF。")

# 示例使用
video_path = 'example.mp4'
gif_path = 'example.gif'
start_time = 10  # 开始时间（秒）
end_time = 20  # 结束时间（秒）

# 从视频中提取帧并创建GIF
extract_frames_and_make_gif(video_path, gif_path, start_time, end_time)

# 使用关键词索引GIF
keyword = 'example'
gif_index = index_gif_with_keyword(gif_path, keyword)

# 用户评论
comment = "这是一个带有关键词的示例评论。"

# 根据检测到的关键词显示相应的GIF
display_gif_for_comment(comment, gif_index)
