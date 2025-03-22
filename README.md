飞机大战游戏 🛩️ https://img.shields.io/badge/license-MIT-blue.svg
基于Pygame开发的经典2D射击游戏，通过方向键控制战机移动，空格键发射三连发子弹击落敌机。本项目包含完整的游戏循环、碰撞检测和爆炸动画系统，适合Python初学者学习游戏开发基础。

./images/game_screenshot.png

功能特性
​玩家控制系统：支持方向键（↑↓←→）实时操控战机移动
​智能敌机AI：敌机自动左右移动并触碰边界转向
​三连发子弹系统：按空格键触发多弹道攻击
​碰撞检测机制：精确判断子弹与敌机的碰撞区域
​爆炸动画序列：6帧高清爆破特效（含资源文件）
​流畅游戏循环：60FPS帧率保证游戏流畅性
快速启动
环境配置
bash
# 安装依赖库（推荐Pygame 2.1.3+）
pip install -r requirements.txt  # 包含：pygame==2.1.3
运行游戏
bash
git clone https://github.com/你的用户名/飞机大战.git
cd 飞机大战
python aircraft_war.py
代码架构解析
核心模块设计
python
# 玩家战机控制（网页3]
def hero_plane():
    global hero_x, hero_y  # 使用全局坐标变量
    # 事件监听处理WASD和空格键
    # 子弹对象存储为字典列表结构

# 敌机行为系统（网页2]
def enemy_plane():
    global enemy_x, enemy_path  # 自动移动路径计算
    # 碰撞检测范围：x轴[enemy_x, enemy_x+165], y轴[0,265]
    # 爆炸动画通过blow_up数组实现帧序列播放
资源管理规范
python
# 资源加载规范（需创建aircraft_war_material目录）
background = pygame.image.load("./aircraft_war_material/background.png") 
hero = pygame.image.load("./aircraft_war_material/hero1.png")
开发路线图
 增加计分系统（击杀敌机得分）
 实现多敌机生成器
 添加音效管理系统
 开发关卡难度递增机制
注意事项
必须保证资源文件目录结构完整
建议屏幕分辨率为400x800像素
游戏速度受time.sleep(0.01)控制，可调整该值改变节奏
碰撞检测区域根据敌机素材尺寸(165x265)设定
贡献指南
欢迎通过Pull Request提交改进：

Fork本仓库
创建特性分支（如feature/enhance-collision）
提交代码变更（需符合PEP8规范）
发起Pull Request
开源协议
本项目采用 MIT License，允许自由使用及二次开发，但需保留原始版权声明。

​学习提示：建议结合《Python核心应用》教程深入理解游戏循环和事件处理机制。开发时推荐使用PyCharm专业版进行调试，可利用其集成的Pygame调试工具加速开发流程。
