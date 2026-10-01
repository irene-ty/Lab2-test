import html
import random

import streamlit as st


st.set_page_config(
    page_title="两个人的故事",
    page_icon="💗",
    layout="centered",
)


STORIES = {
    "浪漫": [
        (
            "{a}与{b}在一场突如其来的春雨里，共撑了同一把伞。"
            "此后，他们总在那家临街书店相遇，一个假装挑书，一个悄悄等人。"
            "夏夜停电时，{b}点亮一串旧灯，{a}才发现每只灯罩上都写着一句想说却没说的话。"
            "多年后，两人搬进有小阳台的房子，依旧把初见那把伞挂在门边。"
            "最好的缘分，是让漫长岁月仍像一次心动的偶遇。"
        ),
        (
            "城市亮起晚灯时，{a}在最后一班电车上遇见了{b}。"
            "他们从同一站下车，又沿着河岸慢慢走了很久。"
            "后来，{a}把每次想念写成便签，悄悄夹进{b}常看的书里；"
            "{b}则把两人错过的日落画成一本小册子。"
            "许多年后，他们仍会并肩看晚霞，因为爱情不是宏大的奇迹，"
            "而是愿意把每个平凡的今天慢慢过亮。"
        ),
    ],
    "搞怪": [
        (
            "{a}和{b}的爱情，始于一杯被拿错的奶茶。"
            "两人见面必斗嘴，聊天记录里三分是表情包，七分是“你等着”。"
            "{b}为了证明自己会做饭，端出一盘形状可疑的煎蛋，"
            "{a}沉默三秒后夸它很有现代艺术气息。"
            "后来他们依然每天拌嘴，只是吵到最后，总有人把最后一块炸鸡留给对方。"
            "爱情有时不是偶像剧，而是一场笑着认输的长期比赛。"
        ),
        (
            "传说月老牵线很准，可轮到{a}和{b}时，他大概顺手打了个死结。"
            "他们约会总会迷路，却坚持不看地图，理由是谁先导航谁就输了。"
            "朋友们设下告白局，结果气球提前爆开，蛋糕当场倒扣，"
            "只有那句“我喜欢你”说得无比清楚。"
            "从此家里多了一条规矩：可以互相吐槽，不许真的生气。"
            "最合拍的爱情，就是有人陪你把日子过成连续喜剧。"
        ),
    ],
    "文艺": [
        (
            "{a}遇见{b}那年，南方的梅雨正把整座城写成一封潮湿的信。"
            "他们在黄昏里散步，很少谈论爱，只谈云的形状、河流的去处和未读完的诗。"
            "秋天来临时，{a}收到一片夹在信里的银杏叶，"
            "背面写着：“所有远方，最后都想抵达你。”"
            "后来，他们在河岸边住下，看季节一次次更换颜色。"
            "爱情不再是句子，而成了窗台的茶、归家的脚步和灯下永远为彼此留着的位置。"
        ),
        (
            "旧车站的钟慢了七分钟，恰好让{a}看见站在梧桐树下的{b}。"
            "他们交换书页与车票，让寻常日子有了可以折叠、收藏和反复阅读的纹理。"
            "时间像一尾缓慢的鱼，从两人的指缝游过，又在每次回望时泛起微光。"
            "他们没有向世界宣告什么，只在每个清晨互道早安。"
            "于是漫长的生活有了押韵，连沉默也像一首终于写完的诗。"
        ),
    ],
    "悲剧": [
        (
            "{a}和{b}约好在初雪那天重逢，可那年冬天，雪迟迟没有落下。"
            "那些没说出口的话，在沉默里越长越深，最终成了谁也跨不过去的河。"
            "许多年后，一封旧信因邮局搬迁被退回，"
            "邮戳已经褪色，纸上的那句“等我”却仍清晰。"
            "后来，{a}偶尔会梦见两人真的赴了约。"
            "醒来时天光安静，身旁空无一人，"
            "只有窗外的雪替他们完成了一场迟到太久的告别。"
        ),
        (
            "{a}离开小城前，把一封信交给旧邮局，"
            "却不知道收信人{b}早已换了地址。"
            "他们曾认真计划每一个明天，"
            "却忘了命运最擅长在人毫无准备时改写结尾。"
            "多年后，{b}仍会经过从前那家咖啡馆，"
            "却再也没有坐进靠窗的第二个位置。"
            "他们都继续向前生活，只是心里永远停着一班没有抵达的列车。"
            "爱没有消失，它只是成了漫长岁月里最安静的遗憾。"
        ),
    ],
    "科幻": [
        (
            "公元2189年，{a}是火星气象站最后一位值守员，"
            "{b}则是从地球发来讯息的深空工程师。"
            "两颗星球之间有十二分钟的通信延迟，"
            "他们的每句思念都抵达得稍晚一些。"
            "太阳风暴来临时，基地与地球失去联系，"
            "{a}却在备用频道里听见{b}提前录好的声音："
            "“无论宇宙多远，我都会回答你。”"
            "当通讯重新亮起，两人在漫天红沙中完成了一场跨越星海的告白。"
        ),
        (
            "{a}在星际航行中醒来，发现飞船已经偏离航线三百年，"
            "唯一陪伴自己的，是保存着{b}记忆的智能系统。"
            "系统会讲旧地球的雨，也会准确记得两人初次见面的日期。"
            "抵达新家园前，飞船能源只够唤醒一个生命舱。"
            "{a}正准备放弃自己，沉睡舱却缓缓打开，"
            "真正的{b}从里面伸出手。"
            "原来漫长宇宙没有带走爱情，"
            "只把重逢变成了一场迟到三百年的奇迹。"
        ),
    ],
}


TITLES = {
    "浪漫": ["晚风知道答案", "星光落在你肩上"],
    "搞怪": ["爱情事故现场", "冤家宜相爱"],
    "文艺": ["潮汐替我记得", "云经过旧窗"],
    "悲剧": ["没寄出的最后一封信", "雪落以前"],
    "科幻": ["星海回信", "相爱于第三颗行星"],
}


def make_story(name_a, name_b, style):
    template = random.choice(STORIES[style])
    story = template.format(a=name_a, b=name_b)

    if len(story) > 200:
        story = story[:199] + "。"

    title = random.choice(TITLES[style])
    return title, story


st.markdown(
    """
    <style>
    .stApp {
        color: #392a43;
        background:
            radial-gradient(
                circle at 12% 12%,
                rgba(255, 208, 222, 0.85),
                transparent 25rem
            ),
            radial-gradient(
                circle at 88% 18%,
                rgba(199, 224, 255, 0.9),
                transparent 28rem
            ),
            linear-gradient(
                145deg,
                #fff9fc 0%,
                #f5f1ff 48%,
                #eef8ff 100%
            );
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 880px;
        padding-top: 3.2rem;
        padding-bottom: 4rem;
    }

    .hero {
        margin-bottom: 1.8rem;
        padding: 1.4rem 0 0.5rem;
        text-align: center;
    }

    .hero-kicker {
        color: #a34769;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            cursive;
        font-size: 1rem;
        letter-spacing: 0.3em;
    }

    .hero-title {
        margin: 0.45rem 0 0.8rem;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            "Yuanti SC",
            cursive;
        font-size: clamp(3rem, 8vw, 5.4rem);
        font-weight: 700;
        line-height: 1.08;
        letter-spacing: 0.02em;
        color: #713953;
        background: linear-gradient(
            105deg,
            #9d3f68,
            #6d56b5 55%,
            #397fa4
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(
            0 8px 20px rgba(123, 69, 111, 0.14)
        );
    }

    .hero-copy {
        color: #78677f;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            cursive;
        font-size: 1.12rem;
        line-height: 1.8;
    }

    div[data-testid="stTextInput"] label,
    div[data-testid="stRadio"] label {
        color: #59455f;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            cursive;
        font-size: 1.02rem;
    }

    div[data-testid="stTextInput"] input {
        min-height: 3.2rem;
        color: #49364e;
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid rgba(142, 93, 132, 0.22);
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(105, 76, 120, 0.07);
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #b56f98;
        box-shadow: 0 0 0 3px rgba(181, 111, 152, 0.13);
    }

    div[data-testid="stRadio"] > div {
        padding: 0.6rem 0.8rem;
        gap: 0.5rem 1rem;
        background: rgba(255, 255, 255, 0.48);
        border: 1px solid rgba(142, 93, 132, 0.14);
        border-radius: 16px;
    }

    .stButton > button {
        width: 100%;
        min-height: 3.35rem;
        color: white;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            cursive;
        font-size: 1.1rem;
        font-weight: 700;
        border: 0;
        border-radius: 16px;
        background: linear-gradient(
            100deg,
            #c15e88,
            #8b69c8 58%,
            #5a9fbd
        );
        box-shadow:
            0 14px 30px rgba(139, 90, 150, 0.25);
    }

    .stButton > button:hover {
        color: white;
        border: 0;
        transform: translateY(-2px);
        filter: brightness(1.05);
    }

    .story-shell {
        margin-top: 2.2rem;
        padding: 1px;
        border-radius: 28px;
        background: linear-gradient(
            135deg,
            rgba(213, 110, 151, 0.7),
            rgba(139, 105, 200, 0.55),
            rgba(90, 159, 189, 0.65)
        );
        box-shadow:
            0 24px 65px rgba(95, 63, 116, 0.2);
    }

    .story-card {
        position: relative;
        overflow: hidden;
        padding: clamp(1.8rem, 5vw, 3.2rem);
        color: #493845;
        background:
            linear-gradient(
                rgba(255, 255, 255, 0.91),
                rgba(255, 255, 255, 0.91)
            ),
            repeating-linear-gradient(
                0deg,
                #f7edf2 0,
                #f7edf2 1px,
                transparent 1px,
                transparent 28px
            );
        border-radius: 27px;
    }

    .story-card::after {
        content: "“";
        position: absolute;
        right: 1rem;
        bottom: -5.5rem;
        color: rgba(153, 73, 113, 0.07);
        font-family: Georgia, serif;
        font-size: 16rem;
        line-height: 1;
    }

    .story-badge {
        display: inline-block;
        position: relative;
        z-index: 1;
        padding: 0.38rem 0.8rem;
        color: #9a4268;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            cursive;
        font-weight: 700;
        letter-spacing: 0.12em;
        border: 1px solid rgba(154, 66, 104, 0.22);
        border-radius: 999px;
        background: #fff7fa;
    }

    .story-title {
        position: relative;
        z-index: 1;
        margin: 1.5rem 0 1rem;
        color: #763b59;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            cursive;
        font-size: clamp(1.8rem, 5vw, 2.55rem);
        letter-spacing: 0.04em;
    }

    .story-text {
        position: relative;
        z-index: 1;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            "Yuanti SC",
            cursive;
        font-size: 1.24rem;
        line-height: 2.05;
        text-align: justify;
        letter-spacing: 0.025em;
    }

    .story-count {
        position: relative;
        z-index: 1;
        margin-top: 1.5rem;
        padding-top: 1rem;
        color: #927e8c;
        font-family:
            "Kaiti SC",
            "STKaiti",
            "KaiTi",
            cursive;
        border-top:
            1px dashed rgba(113, 57, 83, 0.2);
    }

    @media (max-width: 640px) {
        .block-container {
            padding: 1.5rem 1rem 3rem;
        }

        .hero-title {
            font-size: 3.1rem;
        }

        .story-card {
            border-radius: 21px;
        }

        .story-shell {
            border-radius: 22px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <section class="hero">
        <div class="hero-kicker">
            LOVE STORY MAKER
        </div>

        <h1 class="hero-title">
            把名字写进故事里
        </h1>

        <div class="hero-copy">
            填入两个名字或代号，
            选择一种心情，
            让故事从这里开始。
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


left, right = st.columns(2, gap="medium")

with left:
    name_a = st.text_input(
        "名字 A",
        placeholder="例如：小满",
        max_chars=12,
    )

with right:
    name_b = st.text_input(
        "名字 B",
        placeholder="例如：阿青",
        max_chars=12,
    )


style = st.radio(
    "故事风格",
    ["浪漫", "搞怪", "文艺", "悲剧", "科幻"],
    horizontal=True,
)


if st.button(
    "生成我们的故事",
    type="primary",
    use_container_width=True,
):
    name_a = name_a.strip()
    name_b = name_b.strip()

    if not name_a or not name_b:
        st.error("请先输入两个名字或代号。")

    elif name_a == name_b:
        st.error("两个名字最好不一样，故事才有相遇。")

    else:
        title, story = make_story(
            name_a,
            name_b,
            style,
        )

        st.session_state["result"] = {
            "title": title,
            "story": story,
            "style": style,
        }


if "result" in st.session_state:
    result = st.session_state["result"]

    safe_title = html.escape(result["title"])
    safe_story = html.escape(result["story"])
    safe_style = html.escape(result["style"])

    st.markdown(
        f"""
        <div class="story-shell">
            <article class="story-card">
                <span class="story-badge">
                    {safe_style}篇
                </span>

                <h2 class="story-title">
                    《{safe_title}》
                </h2>

                <div class="story-text">
                    {safe_story}
                </div>

                <div class="story-count">
                    {len(result["story"])} 字 · 100–200 字
                </div>
            </article>
        </div>
        """,
        unsafe_allow_html=True,
    )
    