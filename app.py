import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Will You Be My Valentine? 💖", layout="centered")

# Customize her name here 👇
her_name = "My Love"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    text-align: center;
    background: linear-gradient(135deg, #ff4e8a, #ff9eb5);
    font-family: Arial, sans-serif;
    overflow: hidden;
}}

h1 {{
    color: white;
    font-size: 50px;
    margin-top: 100px;
}}

button {{
    padding: 15px 35px;
    font-size: 22px;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    margin: 15px;
    position: absolute;
}}

#yesBtn {{
    background-color: #28a745;
    color: white;
    left: 40%;
    top: 55%;
}}

#noBtn {{
    background-color: #dc3545;
    color: white;
    left: 55%;
    top: 55%;
}}

.heart {{
    position: fixed;
    color: red;
    animation: float 5s linear infinite;
}}

@keyframes float {{
    0% {{ transform: translateY(100vh); }}
    100% {{ transform: translateY(-10vh); }}
}}
</style>
</head>
<body>

<h1>{her_name}, Will You Be My Valentine? 💘</h1>

<button id="yesBtn" onclick="celebrate()">Yes 💖</button>
<button id="noBtn" onmouseover="moveButton()">No 😢</button>

<script>
function moveButton() {{
    var btn = document.getElementById("noBtn");
    var x = Math.random() * (window.innerWidth - 100);
    var y = Math.random() * (window.innerHeight - 50);
    btn.style.left = x + "px";
    btn.style.top = y + "px";
}}

function celebrate() {{
    document.body.innerHTML = `
        <h1 style="color:white;margin-top:200px;font-size:60px;">
        YAYYY 💖😍<br>
        I Love You So Much {her_name} ❤️
        </h1>
    `;
    createHearts();
}}

function createHearts() {{
    for (let i = 0; i < 50; i++) {{
        let heart = document.createElement("div");
        heart.className = "heart";
        heart.innerHTML = "❤️";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.fontSize = (Math.random() * 30 + 20) + "px";
        heart.style.animationDuration = (Math.random() * 3 + 2) + "s";
        document.body.appendChild(heart);
    }}
}}
</script>

</body>
</html>
"""

components.html(html_code, height=800)
