import streamlit as st
# ==========================================

# 1. 🌟 创建左侧边栏导航菜单（在这里加上了 BMI 功能）

# ==========================================

with st.sidebar:

    st.title("导航中心")

    page = st.selectbox(

        "请选择你要进入的功能：",

        ["🏠 欢迎首页", "🎮 心情打游戏检测器", "📖 蔬菜英文查询", "⚖️ BMI 体重健康检测"]

    )
# ==========================================
# 2. 🏠 欢迎首页逻辑
# ==========================================

if page == "🏠 欢迎首页":

    st.title("🚀 GCT的网站")

    st.write("欢迎来到我的 Python 基地！请在左侧边栏选择你想要使用的智能工具。")

    st.info("💡 当前平台已集成了『心情检测』、『蔬菜词典』与『BMI检测』三大核心模块。")

# ==========================================
# 3. 🎮 心情打游戏检测器逻辑
# ==========================================

elif page == "🎮 心情打游戏检测器":

    st.title("🎮 终极求生欲：打游戏检测器")
    my_mood = st.number_input("我的心情指数是:", min_value=0.0, max_value=100.0, value=50.0)
    her_mood = st.number_input("她的心情指数是:", min_value=0.0, max_value=100.0, value=50.0)
    game = my_mood + her_mood
    st.write("今天的心情指数是: " + str(game))
    if game >= 90:
        if my_mood > 40 and her_mood > 40:
            st.success("可以打游戏 😄")
        else:
            st.warning("有人心情不好 ☠️")
    elif 50 <= game < 90:
        if my_mood > 25 and her_mood > 25:
            st.info("可以稍微打一下 🙂")
        else:
            st.warning("最好不要打！！！")
    else:
        st.error("你打一下试试 ☠️")
# ==========================================
# 4. 📖 蔬菜英文查询逻辑
# ==========================================
elif page == "📖 蔬菜英文查询":
    st.title("📖 蔬菜英文查询百科")
    vegetable_dict = {"土豆": "potato", "西红柿": "tomato"}
    vegetable_dict["胡萝卜"] = "carrot"
    vegetable_dict["白菜"] = "Chinese cabbage"
    vegetable_dict["黄瓜"] = "cucumber"
    vegetable_dict["洋葱"] = "onion"
    vegetable_dict["菠菜"] = "spinach"
    vegetable_dict["青椒"] = "green pepper"
    query = st.text_input("请输入您想要查询的蔬菜中文名：")
    if query:
        if query in vegetable_dict:
            st.write("您查询的 " + query + " 英文含义如下：")
            st.info(vegetable_dict[query])
        else:
            st.error("您查询的单词我们暂未收录 ❌")
            st.warning("当前本词典收录的词条数量为：" + str(len(vegetable_dict)) + " 条。")
# ==========================================
# 5. ⚖️ BMI 体重健康检测逻辑（全新塞入！）
# ==========================================
elif page == "⚖️ BMI 体重健康检测":
    st.title("⚖️ BMI 身体质量指数检测")
    # 把原本的 input 升级为网页数字输入框，并贴心地设置了默认值
    high = st.number_input("请输入您的身高（单位：m）：", min_value=0.5, max_value=2.5, value=1.75)
    weight = st.number_input("请输入您的体重（单位：kg）：", min_value=10.0, max_value=200.0, value=65.0)
    # 核心数学公式完全不变
    use_BMI = weight / (high ** 2)
    # 保留两位小数打印，看起来更专业
    st.write(f"您的 BMI 指数是：{use_BMI:.2f}")
    # 你的原装 if-elif 逻辑，配上最生动的彩色气泡框！
    if use_BMI >= 28:
        st.error("检测结果：肥胖 🚨 请注意饮食与运动哦！")  # 🔴 红色危险
    elif 24 < use_BMI < 28:
        st.warning("检测结果：超重 ⚠️ 稍微有些微胖啦！")  # 🟡 黄色警告
    elif 18.5 < use_BMI <= 24:
        st.success("检测结果：体重正常 🎉 太棒了，继续保持！")  # 🟢 绿色成功
    else:
        st.info("检测结果：体重过低 ℹ️ 要多吃点营养品哦！")  # 🔵 蓝色提示