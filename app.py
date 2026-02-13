import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="A Special Surprise 💖", layout="centered")

her_name = "My Princess"   # 👈 CHANGE THIS
your_name = "Your King"    # 👈 CHANGE THIS

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body {{
    margin: 0;
    padding: 0;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    background-image: url('https://images.unsplash.com/photo-1518199266791-5375a83190b7');
    background-size: cover;
    background-position: center;
    color: white;
    overflow: hidden;
}}

.overlay {{
    background: rgba(0,0,0,0.6);
    position: absolute;
    width: 100%;
    height: 100%;
}}

.container {{
    position: relative;
    top: 20%;
    z-index: 2;
}}

h1 {{
    font-size: 55px;
}}

button {{
    padding: 15px 35px;
    font-size: 20px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    margin: 10px;
    position: relative;
}}

#yesBtn {{
    background-color: #ff4e8a;
    color: white;
}}

#noBtn {{
    background-color: #555;
    color: white;
    position: absolute;
}}

.quiz {{
    margin-top: 20px;
}}

.heart {{
    position: fixed;
    font-size: 30px;
    animation: float 4s linear infinite;
}}

@keyframes float {{
    0% {{ transform: translateY(100vh); }}
    100% {{ transform: translateY(-10vh); }}
}}

.firework {{
    position: fixed;
    width: 10px;
    height: 10px;
    background: yellow;
    border-radius: 50%;
    animation: explode 1s ease-out forwards;
}}

@keyframes explode {{
    0% {{ transform: scale(1); opacity:1; }}
    100% {{ transform: scale(15); opacity:0; }}
}}
</style>
</head>

<body>

<div class="overlay"></div>

<div class="container">

<h1 id="typewriter"></h1>

<div class="quiz" id="quizSection">
    <p>First answer this 😏</p>
    <p>Who loves you the most?</p>
    <button onclick="correct()"> {your_name} 💖 </button>
    <button onclick="wrong()"> Someone Else 😢 </button>
</div>

<div id="proposal" style="display:none;">
    <h1>{her_name}, Will You Be My Valentine? 💘</h1>
    <button id="yesBtn" onclick="celebrate()">YESSS 💖</button>
    <button id="noBtn" onmouseover="moveNo()">No 😭</button>
</div>

</div>

<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
</audio>

<script>
let text = "Hey {her_name}... I have something special for you 💌";
let i = 0;
function typeWriter() {{
    if (i < text.length) {{
        document.getElementById("typewriter").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, 60);
    }}
}}
typeWriter();

function correct() {{
    document.getElementById("quizSection").style.display = "none";
    document.getElementById("proposal").style.display = "block";
}}

function wrong() {{
    alert("Wrong answer 😏 Try again!");
}}

function moveNo() {{
    let btn = document.getElementById("noBtn");
    btn.style.position = "absolute";
    btn.style.left = Math.random() * 80 + "%";
    btn.style.top = Math.random() * 80 + "%";
}}

function celebrate() {{
    document.body.innerHTML = `
        <h1 style="margin-top:200px;font-size:60px;color:white;">
        SHE SAID YESSS 😍💖<br>
        I Love You Forever {her_name} ❤️
        </h1>
    `;
    for(let i=0;i<30;i++) {{
        let heart = document.createElement("div");
        heart.className="heart";
        heart.innerHTML="❤️";
        heart.style.left=Math.random()*100+"vw";
        heart.style.animationDuration=(Math.random()*3+2)+"s";
        document.body.appendChild(heart);

        let fire=document.createElement("div");
        fire.className="firework";
        fire.style.left=Math.random()*100+"vw";
        fire.style.top=Math.random()*100+"vh";
        document.body.appendChild(fire);
    }}
}}
</script>

</body>
</html>
"""

components.html(html_code, height=900)
