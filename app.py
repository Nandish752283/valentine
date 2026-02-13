import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Netflix Valentine Finale 💖", layout="wide")

# ==== CUSTOMIZE THESE ====
her_name = "My Princess"
your_name = "Your King"
photos = [
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e",
    "https://images.unsplash.com/photo-1507874457470-272b3c8d8ee2",
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e"
]

# ==== HTML + JS ====
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>💘 Netflix Valentine Finale 💘</title>
<style>
html, body {{
    margin:0; padding:0;
    width:100%; height:100%;
    overflow:hidden;
    font-family: 'Segoe UI', sans-serif;
    background:black;
    color:white;
}}

#loadingScreen {{
    position:fixed;
    width:100%; height:100%;
    background:black;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    font-size:50px;
    z-index:10;
}}

#mainContent {{
    display:none;
    width:100%; height:100%;
    position:relative;
}}

#slideshow {{
    position:absolute;
    width:100%; height:100%;
    overflow:hidden;
    z-index:-1;
}}

.slide {{
    position:absolute;
    width:100%; height:100%;
    background-size:cover;
    background-position:center;
    opacity:0;
    transition: opacity 1.5s;
}}

#countdown {{
    position:absolute;
    top:20px; left:50%;
    transform:translateX(-50%);
    font-size:35px;
    background:rgba(0,0,0,0.4);
    padding:10px 20px;
    border-radius:15px;
}}

#hiddenMessage {{
    display:none;
    position:absolute;
    top:50%; left:50%;
    transform:translate(-50%,-50%);
    font-size:40px;
    background:rgba(255,255,255,0.3);
    padding:20px;
    border-radius:20px;
}}

#proposalScreen {{
    display:none;
    width:100%; height:100%;
    position:absolute;
    top:0; left:0;
    background:black;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    display:flex;
    font-size:50px;
    z-index:20;
    color:#ff4e8a;
}}

#gameScreen {{
    display:none;
    width:100%; height:100%;
    position:absolute;
    top:0; left:0;
    background:rgba(0,0,0,0.9);
    justify-content:center;
    align-items:center;
    flex-direction:column;
    display:flex;
    z-index:15;
}}

.heart {{
    position:absolute;
    font-size:30px;
    cursor:pointer;
    user-select:none;
}}

</style>
</head>

<body>

<div id="loadingScreen">
    Loading Love Experience... 💖
</div>

<div id="mainContent">

    <div id="slideshow"></div>

    <div id="countdown"></div>

    <div id="hiddenMessage">
        You found the secret message! I ❤️ you {her_name}!
    </div>

    <div id="gameScreen">
        <h1>Collect Hearts to Unlock 💌</h1>
        <p>Click on all hearts to unlock the proposal!</p>
        <div id="heartsContainer"></div>
    </div>

    <div id="proposalScreen">
        💖 {her_name}, Will You Be My Valentine? 💍<br>
        <button onclick="sayYes()" style="font-size:30px;padding:20px;border-radius:15px;background:#28a745;color:white;border:none;margin-top:20px;cursor:pointer;">YESSS 💖</button>
        <button id="noBtn" style="font-size:30px;padding:20px;border-radius:15px;background:#555;color:white;border:none;position:absolute;top:50%;left:50%;margin-left:200px;">NO 😭</button>
    </div>

</div>

<script>
// ==== Loading Screen ====
setTimeout(() => {{
    document.getElementById('loadingScreen').style.display='none';
    document.getElementById('mainContent').style.display='block';
    startSlideshow();
    startCountdown();
    showGame();
}}, 3000);

// ==== Slideshow ====
const photos = {photos};
function startSlideshow() {{
    const container = document.getElementById('slideshow');
    photos.forEach((url,i)=>{{
        let div = document.createElement('div');
        div.className='slide';
        div.style.backgroundImage='url('+url+')';
        container.appendChild(div);
    }});
    let current=0;
    container.children[current].style.opacity=1;
    setInterval(()=>{{
        container.children[current].style.opacity=0;
        current=(current+1)%container.children.length;
        container.children[current].style.opacity=1;
    }},4000);
}}

// ==== Countdown ====
function startCountdown() {{
    const countdown = document.getElementById('countdown');
    const target = new Date(new Date().getFullYear(),1,14); // Feb 14
    setInterval(()=>{{
        let now=new Date();
        let diff=target-now;
        let d=Math.floor(diff/1000/60/60/24);
        let h=Math.floor(diff/1000/60/60)%24;
        let m=Math.floor(diff/1000/60)%60;
        let s=Math.floor(diff/1000)%60;
        countdown.innerHTML=`Valentine's in ${{d}}d ${{h}}h ${{m}}m ${{s}}s`;
    }},1000);
}}

// ==== Hidden Message ====
document.body.addEventListener('click',(e)=>{{
    if(Math.random()<0.01){{
        document.getElementById('hiddenMessage').style.display='block';
    }}
}});

// ==== Heart Collect Game ====
function showGame(){{
    const game=document.getElementById('gameScreen');
    game.style.display='flex';
    const container=document.getElementById('heartsContainer');
    let hearts=[];
    for(let i=0;i<10;i++){{
        let heart=document.createElement('div');
        heart.className='heart';
        heart.innerHTML='❤️';
        heart.style.left=Math.random()*90+'vw';
        heart.style.top=Math.random()*80+'vh';
        heart.onclick=function(){{
            heart.style.display='none';
            hearts[i]=true;
            if(hearts.filter(Boolean).length==10){{
                game.style.display='none';
                showProposal();
            }}
        }};
        container.appendChild(heart);
        hearts.push(false);
    }}
}}

// ==== Proposal Screen ====
function showProposal(){{
    const proposal=document.getElementById('proposalScreen');
    proposal.style.display='flex';
    const noBtn=document.getElementById('noBtn');
    noBtn.addEventListener('mouseover',()=>{
        noBtn.style.left=Math.random()*80+'vw';
        noBtn.style.top=Math.random()*80+'vh';
    });
}}

function sayYes(){{
    document.getElementById('proposalScreen').innerHTML=`<h1 style="font-size:60px;">💖 SHE SAID YES! 💖<br>I Love You Forever {her_name} 💍</h1>`;
    for(let i=0;i<50;i++){{
        let heart=document.createElement('div');
        heart.className='heart';
        heart.innerHTML='❤️';
        heart.style.left=Math.random()*100+'vw';
        heart.style.top=Math.random()*100+'vh';
        heart.style.fontSize=(Math.random()*40+20)+'px';
        document.body.appendChild(heart);
    }}
}}
</script>

</body>
</html>
"""

components.html(html_code, height=1000)
