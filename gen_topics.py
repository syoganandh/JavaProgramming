import os
BASE = "/sessions/kind-inspiring-goodall/mnt/java GIT"

BRAND = "Sampathirao Software Solutions"

NAV_LINKS = [
    ("java_w01.html","Week 1&2: OOP Fundamentals"),
    ("java_w03.html","Week 3: Java Language Basics"),
    ("java_w04.html","Week 4&5: Classes & Objects"),
    ("java_w06.html","Week 6: Static, this, final & Strings"),
    ("java_w07.html","Week 7: Inheritance & Polymorphism"),
    ("java_w08.html","Week 8: Interfaces"),
    ("java_w09.html","Week 9: Packages"),
    ("java_w10.html","Week 10: I/O Streams"),
    ("java_w11.html","Week 11: Exception Handling"),
    ("java_w12.html","Week 12: Multithreading"),
    ("java_w13.html","Week 13: Collection Interfaces"),
    ("java_w14.html","Week 14: Collection Classes"),
]

def shell(css=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--bg:#0F1117;--surf:#181C27;--surf2:#1F2333;--bdr:#2A2F42;--acc:#F07C3E;--gold:#E8C06A;--txt:#E8EAF0;--muted:#6B7194;--grn:#4ECBA0;--blu:#5BA8F5;--red:#F05C5C;--prp:#A97DF5}}
body{{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--txt);line-height:1.7;font-size:15px}}
a{{color:var(--acc);text-decoration:none}}a:hover{{color:var(--gold)}}
.topbar{{background:var(--surf);border-bottom:1px solid var(--bdr);padding:12px 32px;display:flex;align-items:center;gap:14px;position:sticky;top:0;z-index:100}}
.back-btn{{display:flex;align-items:center;gap:5px;color:var(--muted);font-size:.85em;padding:6px 12px;border:1px solid var(--bdr);border-radius:7px;transition:.2s}}
.back-btn:hover{{color:var(--txt);border-color:var(--acc)}}
.brand{{margin-left:auto;font-size:.78em;color:var(--muted)}}
.brand span{{color:var(--gold);font-weight:700}}
.hero{{background:linear-gradient(135deg,#181C27 60%,#1a1530);border-bottom:1px solid var(--bdr);padding:40px 32px 28px}}
.hero .week-badge{{display:inline-block;background:rgba(240,124,62,.12);border:1px solid rgba(240,124,62,.3);color:var(--acc);font-size:.75em;font-weight:700;padding:3px 12px;border-radius:20px;letter-spacing:.06em;margin-bottom:12px}}
.hero h1{{font-size:2em;font-weight:800;letter-spacing:-.02em;background:linear-gradient(120deg,#E8EAF0 40%,#E8C06A);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:8px}}
.hero p{{color:var(--muted);font-size:.9em}}
.co-pill{{display:inline-block;padding:2px 10px;border-radius:5px;font-size:.75em;font-weight:700;margin-left:10px}}
.co1{{background:rgba(78,203,160,.12);color:var(--grn)}}.co2{{background:rgba(91,168,245,.12);color:var(--blu)}}
.co3{{background:rgba(169,125,245,.12);color:var(--prp)}}.co4{{background:rgba(232,192,106,.12);color:var(--gold)}}
.layout{{display:grid;grid-template-columns:220px 1fr;gap:0;max-width:1200px;margin:0 auto;min-height:calc(100vh - 180px)}}
.sidebar{{padding:24px 16px;border-right:1px solid var(--bdr);position:sticky;top:57px;height:calc(100vh - 57px);overflow-y:auto}}
.sidebar h3{{font-size:.7em;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-bottom:10px}}
.toc-list{{list-style:none}}
.toc-list li a{{display:block;padding:5px 8px;font-size:.82em;color:var(--muted);border-radius:6px;transition:.15s}}
.toc-list li a:hover{{background:var(--surf2);color:var(--txt)}}
.toc-list li a.active{{background:rgba(240,124,62,.1);color:var(--acc)}}
.content{{padding:32px 40px 60px;max-width:860px}}
h2{{font-size:1.35em;font-weight:700;color:var(--txt);margin:36px 0 14px;padding-bottom:8px;border-bottom:2px solid var(--bdr);display:flex;align-items:center;gap:10px}}
h2::before{{content:attr(data-icon);font-size:1.1em}}
h3{{font-size:1.05em;font-weight:700;color:var(--gold);margin:22px 0 10px}}
h4{{font-size:.95em;font-weight:700;color:var(--acc);margin:16px 0 6px}}
p{{margin-bottom:12px;color:#C8CAD8}}
ul,ol{{margin:8px 0 12px 22px;color:#C8CAD8}}
li{{margin-bottom:5px}}
.note-box{{background:rgba(78,203,160,.07);border:1px solid rgba(78,203,160,.25);border-radius:10px;padding:14px 18px;margin:16px 0}}
.warn-box{{background:rgba(240,92,92,.07);border:1px solid rgba(240,92,92,.25);border-radius:10px;padding:14px 18px;margin:16px 0}}
.info-box{{background:rgba(91,168,245,.07);border:1px solid rgba(91,168,245,.25);border-radius:10px;padding:14px 18px;margin:16px 0}}
.note-box strong,.warn-box strong,.info-box strong{{font-size:.78em;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:6px}}
.note-box strong{{color:var(--grn)}}.warn-box strong{{color:var(--red)}}.info-box strong{{color:var(--blu)}}
pre{{background:var(--surf2);border:1px solid var(--bdr);border-radius:10px;padding:18px 20px;overflow-x:auto;margin:12px 0 20px;font-size:.85em;line-height:1.6}}
code{{font-family:'Cascadia Code','Fira Code',Consolas,monospace;color:#C8CAD8}}
pre code{{color:#C8CAD8}}
.kw{{color:#C792EA}}.cm{{color:#546E7A;font-style:italic}}.str{{color:#C3E88D}}.num{{color:#F78C6C}}.cls{{color:#FFCB6B}}.fn{{color:#82AAFF}}.ann{{color:#F07C3E}}
table{{width:100%;border-collapse:collapse;margin:14px 0 20px;font-size:.88em}}
th{{background:var(--surf2);color:var(--gold);padding:10px 14px;text-align:left;border-bottom:2px solid var(--bdr)}}
td{{padding:9px 14px;border-bottom:1px solid var(--bdr);color:#C8CAD8}}
tr:hover td{{background:rgba(255,255,255,.02)}}
.pdf-section{{margin-top:48px;padding:24px;background:var(--surf);border:1px solid var(--bdr);border-radius:14px;display:flex;align-items:center;gap:20px}}
.pdf-icon{{font-size:2.4em;flex-shrink:0}}
.pdf-info h3{{color:var(--txt);font-size:1em;margin-bottom:4px}}
.pdf-info p{{color:var(--muted);font-size:.82em;margin:0}}
.pdf-btn{{margin-left:auto;padding:11px 24px;background:var(--acc);border:none;border-radius:9px;color:#111;font-weight:700;font-size:.88em;cursor:pointer;display:flex;align-items:center;gap:7px;white-space:nowrap;transition:.15s;flex-shrink:0}}
.pdf-btn:hover{{background:var(--gold)}}
.nav-bottom{{display:flex;justify-content:space-between;margin-top:40px;padding-top:24px;border-top:1px solid var(--bdr)}}
.nav-btn{{display:flex;align-items:center;gap:8px;padding:10px 18px;background:var(--surf);border:1px solid var(--bdr);border-radius:9px;color:var(--muted);font-size:.85em;transition:.2s}}
.nav-btn:hover{{border-color:var(--acc);color:var(--txt)}}
.nav-btn.next{{flex-direction:row-reverse;text-align:right}}
@media print{{
  .topbar,.sidebar,.pdf-section,.nav-bottom{{display:none!important}}
  body{{background:#fff;color:#000;font-size:12pt}}
  .hero{{background:#f5f5f5;border:none;padding:20px}}
  .hero h1{{-webkit-text-fill-color:#1a1a1a;font-size:1.5em}}
  .content{{padding:10px;max-width:100%}}
  pre{{background:#f5f5f5;border:1px solid #ddd;font-size:9pt}}
  h2{{border-bottom:2px solid #ccc;color:#1a1a1a}}
  h3{{color:#333}}p,li,td{{color:#222}}
  .note-box{{background:#e8f5e9;border:1px solid #4caf50}}
  .info-box{{background:#e3f2fd;border:1px solid #2196f3}}
  .warn-box{{background:#fce4ec;border:1px solid #e91e63}}
  .layout{{display:block}}
  @page{{margin:1.5cm}}
}}
{css}
</style>
</head>"""

def body_open(week_label, title, co_class, co_label, desc, toc_items, prev_link, prev_title, next_link, next_title):
    toc_html = "\n".join(f'<li><a href="#{slug(t)}">{t}</a></li>' for t in toc_items)
    prev_btn = f'<a class="nav-btn" href="{prev_link}">← {prev_title}</a>' if prev_link else '<span></span>'
    next_btn = f'<a class="nav-btn next" href="{next_link}">{next_title} →</a>' if next_link else '<span></span>'
    return f"""
<body>
<div class="topbar">
  <a class="back-btn" href="courses.html">← Back to Courses</a>
  <div class="brand">© 2025 <span>{BRAND}</span></div>
</div>
<div class="hero">
  <div class="week-badge">{week_label}</div>
  <h1>{title}</h1>
  <p>{desc} &nbsp;<span class="co-pill {co_class}">{co_label}</span></p>
</div>
<div class="layout">
  <aside class="sidebar">
    <h3>Contents</h3>
    <ul class="toc-list">{toc_html}</ul>
  </aside>
  <main class="content">
"""

def body_close(prev_link, prev_title, next_link, next_title):
    prev_btn = f'<a class="nav-btn" href="{prev_link}">← {prev_title}</a>' if prev_link else '<span></span>'
    next_btn = f'<a class="nav-btn next" href="{next_link}">{next_title} →</a>' if next_link else '<span></span>'
    return f"""
    <div class="pdf-section">
      <div class="pdf-icon">📄</div>
      <div class="pdf-info">
        <h3>Download PDF Notes</h3>
        <p>Save these notes as a PDF for offline reference</p>
      </div>
      <button class="pdf-btn" onclick="printNotes()">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        Save as PDF
      </button>
    </div>
    <div class="nav-bottom">
      {prev_btn}
      {next_btn}
    </div>
  </main>
</div>
<script>
function printNotes(){{window.print()}}
const sections=document.querySelectorAll('h2[id]');
const links=document.querySelectorAll('.toc-list a');
function onScroll(){{
  let cur='';
  sections.forEach(s=>{{if(window.scrollY>=s.offsetTop-80)cur=s.id}});
  links.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+cur));
}}
window.addEventListener('scroll',onScroll,{{passive:true}});
</script>
</body></html>"""

def slug(t):
    return t.lower().replace(' ','_').replace('&','and').replace('/','_').replace(',','').replace("'","")

def sec(icon, title, content):
    return f'<h2 id="{slug(title)}" data-icon="{icon}">{title}</h2>\n{content}'

def code(c):
    return f'<pre><code>{c}</code></pre>'

def note(msg): return f'<div class="note-box"><strong>📌 Key Point</strong>{msg}</div>'
def warn(msg): return f'<div class="warn-box"><strong>⚠️ Important</strong>{msg}</div>'
def info(msg): return f'<div class="info-box"><strong>💡 Did You Know</strong>{msg}</div>'


# ═══════════════════════════════════════════════════════
# PAGE 1 — Week 1 & 2: OOP Fundamentals
# ═══════════════════════════════════════════════════════
toc1 = ["What is OOP?","Object-Oriented Paradigm","Objects and Classes","Encapsulation","Abstraction","Inheritance","Polymorphism","Dynamic Binding","Advantages of OOP"]

c1 = shell()
c1 += body_open("Week 1 & 2 · CO-1","OOP Fundamentals","co1","CO-1",
    "Object-Oriented Paradigm, Objects & Classes, Encapsulation, Inheritance, Polymorphism, Dynamic Binding",
    toc1,"","","java_w03.html","Week 3: Java Language Basics")

c1 += sec("🏛️","What is OOP?","""
<p>Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around <strong>data</strong>, or <em>objects</em>, rather than functions and logic. An object is an entity that has state (fields) and behaviour (methods).</p>
<p>OOP was designed to overcome the limitations of Procedure-Oriented Programming (POP). In POP, data and functions are separate and data can be accessed by any function — making large programs difficult to manage and prone to errors.</p>
<table>
<tr><th>POP (Procedure-Oriented)</th><th>OOP (Object-Oriented)</th></tr>
<tr><td>Program divided into functions</td><td>Program divided into objects</td></tr>
<tr><td>Data moves freely between functions</td><td>Data is hidden inside objects (encapsulation)</td></tr>
<tr><td>Top-down approach</td><td>Bottom-up approach</td></tr>
<tr><td>Less secure — global data</td><td>More secure — data hiding</td></tr>
<tr><td>Examples: C, Pascal, COBOL</td><td>Examples: Java, C++, Python</td></tr>
</table>
""")

c1 += sec("🔭","Object-Oriented Paradigm","""
<p>The OOP paradigm is built on four main pillars:</p>
<ul>
<li><strong>Encapsulation</strong> — bundling data and methods together; hiding internal details</li>
<li><strong>Abstraction</strong> — showing only essential features; hiding complexity</li>
<li><strong>Inheritance</strong> — acquiring properties from a parent class</li>
<li><strong>Polymorphism</strong> — one interface, many forms</li>
</ul>
""")

c1 += sec("📦","Objects and Classes","""
<h3>Class</h3>
<p>A <strong>class</strong> is a blueprint or template for creating objects. It defines the data (fields) and behaviour (methods) that its objects will have. A class does not occupy memory by itself.</p>
<h3>Object</h3>
<p>An <strong>object</strong> is an instance of a class — a real-world entity created from the class blueprint. Each object has its own copy of instance variables and shares class methods.</p>
"""+code("""<span class="kw">class</span> <span class="cls">Student</span> {
    <span class="cm">// Fields (state)</span>
    <span class="kw">int</span> rollNo;
    <span class="cls">String</span> name;
    <span class="kw">double</span> marks;

    <span class="cm">// Method (behaviour)</span>
    <span class="kw">void</span> <span class="fn">display</span>() {
        <span class="cls">System</span>.out.println(<span class="str">"Roll: "</span> + rollNo + <span class="str">" Name: "</span> + name);
    }
}

<span class="kw">public class</span> <span class="cls">Main</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="cls">Student</span> s1 = <span class="kw">new</span> <span class="cls">Student</span>(); <span class="cm">// object creation</span>
        s1.rollNo = <span class="num">101</span>;
        s1.name = <span class="str">"Arjun"</span>;
        s1.marks = <span class="num">92.5</span>;
        s1.<span class="fn">display</span>();
    }
}""")+note("A class is a logical entity; an object is a physical entity. Memory is allocated only when an object is created using the <code>new</code> keyword."))

c1 += sec("🔒","Encapsulation","""
<p><strong>Encapsulation</strong> is the mechanism of wrapping data (variables) and code (methods) together as a single unit. It protects data from direct access by outside code by making fields <code>private</code> and providing <code>public</code> getter/setter methods.</p>
"""+code("""<span class="kw">class</span> <span class="cls">BankAccount</span> {
    <span class="kw">private double</span> balance; <span class="cm">// hidden from outside</span>

    <span class="kw">public void</span> <span class="fn">deposit</span>(<span class="kw">double</span> amount) {
        <span class="kw">if</span> (amount > <span class="num">0</span>) balance += amount;
    }

    <span class="kw">public double</span> <span class="fn">getBalance</span>() {
        <span class="kw">return</span> balance; <span class="cm">// controlled access</span>
    }
}""")+note("Encapsulation = Data Hiding + Data Binding. It increases security and maintains integrity of data."))

c1 += sec("🎭","Abstraction","""
<p><strong>Abstraction</strong> means hiding the implementation details and showing only the functionality to the user. It reduces complexity and allows the programmer to focus on <em>what</em> an object does instead of <em>how</em> it does it.</p>
<p>In Java, abstraction is achieved through:</p>
<ul>
<li><strong>Abstract classes</strong> (0% to 100% abstraction)</li>
<li><strong>Interfaces</strong> (100% abstraction in older Java)</li>
</ul>
"""+info("Example: When you press the accelerator in a car, you don't need to know the internal combustion process — you just use the interface. That's abstraction."))

c1 += sec("🔗","Inheritance","""
<p><strong>Inheritance</strong> is the mechanism by which one class acquires the properties (fields) and behaviours (methods) of another class. It promotes <strong>code reusability</strong>.</p>
<ul>
<li>The class that is inherited from is called the <strong>Parent / Super / Base</strong> class</li>
<li>The class that inherits is called the <strong>Child / Sub / Derived</strong> class</li>
</ul>
"""+code("""<span class="kw">class</span> <span class="cls">Animal</span> {
    <span class="kw">void</span> <span class="fn">eat</span>() { <span class="cls">System</span>.out.println(<span class="str">"Animal eats"</span>); }
}

<span class="kw">class</span> <span class="cls">Dog</span> <span class="kw">extends</span> <span class="cls">Animal</span> { <span class="cm">// inherits Animal</span>
    <span class="kw">void</span> <span class="fn">bark</span>() { <span class="cls">System</span>.out.println(<span class="str">"Dog barks"</span>); }
}

<span class="cls">Dog</span> d = <span class="kw">new</span> <span class="cls">Dog</span>();
d.<span class="fn">eat</span>();  <span class="cm">// inherited method</span>
d.<span class="fn">bark</span>(); <span class="cm">// own method</span>"""))

c1 += sec("🎨","Polymorphism","""
<p><strong>Polymorphism</strong> means "many forms". It allows a single action to behave differently based on the object it is acting upon.</p>
<h3>Types of Polymorphism in Java</h3>
<table>
<tr><th>Type</th><th>Also Called</th><th>Resolved At</th><th>Achieved By</th></tr>
<tr><td>Compile-time</td><td>Static / Early Binding</td><td>Compile time</td><td>Method Overloading</td></tr>
<tr><td>Runtime</td><td>Dynamic / Late Binding</td><td>Runtime</td><td>Method Overriding</td></tr>
</table>
"""+code("""<span class="cm">// Compile-time polymorphism (Overloading)</span>
<span class="kw">class</span> <span class="cls">Calculator</span> {
    <span class="kw">int</span> <span class="fn">add</span>(<span class="kw">int</span> a, <span class="kw">int</span> b) { <span class="kw">return</span> a + b; }
    <span class="kw">double</span> <span class="fn">add</span>(<span class="kw">double</span> a, <span class="kw">double</span> b) { <span class="kw">return</span> a + b; }
    <span class="kw">int</span> <span class="fn">add</span>(<span class="kw">int</span> a, <span class="kw">int</span> b, <span class="kw">int</span> c) { <span class="kw">return</span> a + b + c; }
}"""))

c1 += sec("⚡","Dynamic Binding","""
<p><strong>Dynamic Binding</strong> (or Late Binding) means that the method to be called is determined at <strong>runtime</strong>, not compile time. This is the basis of runtime polymorphism in Java.</p>
<p>When a parent class reference holds a child class object, and an overridden method is called, Java uses the actual object type (not the reference type) to decide which method to call.</p>
"""+code("""<span class="kw">class</span> <span class="cls">Bank</span> {
    <span class="kw">double</span> <span class="fn">getRate</span>() { <span class="kw">return</span> <span class="num">0</span>; }
}
<span class="kw">class</span> <span class="cls">SBI</span> <span class="kw">extends</span> <span class="cls">Bank</span> {
    <span class="kw">double</span> <span class="fn">getRate</span>() { <span class="kw">return</span> <span class="num">7.0</span>; }
}
<span class="kw">class</span> <span class="cls">HDFC</span> <span class="kw">extends</span> <span class="cls">Bank</span> {
    <span class="kw">double</span> <span class="fn">getRate</span>() { <span class="kw">return</span> <span class="num">6.5</span>; }
}

<span class="cls">Bank</span> b = <span class="kw">new</span> <span class="cls">SBI</span>(); <span class="cm">// parent ref → child object</span>
<span class="cls">System</span>.out.println(b.<span class="fn">getRate</span>()); <span class="cm">// prints 7.0 — decided at runtime</span>
b = <span class="kw">new</span> <span class="cls">HDFC</span>();
<span class="cls">System</span>.out.println(b.<span class="fn">getRate</span>()); <span class="cm">// prints 6.5</span>""")+note("Dynamic binding enables runtime polymorphism. The JVM checks the actual object type at runtime and calls the appropriate overridden method."))

c1 += sec("✅","Advantages of OOP","""
<ul>
<li><strong>Modularity</strong> — Each object is self-contained; easy to locate and fix bugs</li>
<li><strong>Reusability</strong> — Classes can be reused in different programs via inheritance</li>
<li><strong>Security</strong> — Data encapsulation hides internal details from the outside</li>
<li><strong>Flexibility</strong> — Polymorphism makes code adaptable to different situations</li>
<li><strong>Maintainability</strong> — OOP code is easier to maintain and upgrade</li>
<li><strong>Real-world modeling</strong> — Objects map naturally to real-world entities</li>
</ul>
""")

c1 += body_close("","","java_w03.html","Week 3: Java Language Basics")
with open(f"{BASE}/java_w01.html","w",encoding="utf-8") as f:
    f.write(c1)
print("✅ java_w01.html")

# ═══════════════════════════════════════════════════════
# PAGE 2 — Week 3: Java Language Basics
# ═══════════════════════════════════════════════════════
toc2 = ["Java Buzzwords","Data Types","Variables","Operators","Control Structures","Arrays","Console I/O"]
c2 = shell()
c2 += body_open("Week 3 · CO-1","Java Language Basics","co1","CO-1",
    "Buzzwords, Data Types, Variables, Operators, Control Structures, Arrays, Console I/O",
    toc2,"java_w01.html","Week 1&2: OOP Fundamentals","java_w04.html","Week 4&5: Classes & Objects")

c2 += sec("☕","Java Buzzwords","""
<p>Java was designed with specific goals that make it unique. These goals are described as Java's <strong>Buzzwords</strong>:</p>
<table>
<tr><th>Buzzword</th><th>Meaning</th></tr>
<tr><td><strong>Simple</strong></td><td>Syntax similar to C/C++ but without complex features like pointers and operator overloading</td></tr>
<tr><td><strong>Object-Oriented</strong></td><td>Everything in Java is an object; supports all OOP features</td></tr>
<tr><td><strong>Platform Independent</strong></td><td>Write Once, Run Anywhere (WORA) — bytecode runs on any JVM</td></tr>
<tr><td><strong>Secured</strong></td><td>No explicit pointers; bytecode verification; security manager</td></tr>
<tr><td><strong>Robust</strong></td><td>Strong exception handling; no pointer arithmetic; automatic garbage collection</td></tr>
<tr><td><strong>Architecture Neutral</strong></td><td>Bytecode is not specific to any processor architecture</td></tr>
<tr><td><strong>Portable</strong></td><td>Platform-independent + architecture-neutral = portable</td></tr>
<tr><td><strong>High Performance</strong></td><td>JIT (Just-In-Time) compiler converts bytecode to native code at runtime</td></tr>
<tr><td><strong>Distributed</strong></td><td>Supports networking protocols; RMI; enterprise distribution</td></tr>
<tr><td><strong>Multi-threaded</strong></td><td>Built-in support for multithreading</td></tr>
<tr><td><strong>Dynamic</strong></td><td>Classes loaded dynamically at runtime; supports runtime polymorphism</td></tr>
</table>
"""+note("The most important buzzword is <strong>Platform Independence</strong>. Java achieves this via the JVM — Java source → javac compiler → bytecode (.class) → JVM → executes on any OS."))

c2 += sec("🔢","Data Types","""
<p>Java is a <strong>strongly typed</strong> language — every variable must have a declared type.</p>
<h3>Primitive Data Types (8 types)</h3>
<table>
<tr><th>Type</th><th>Size</th><th>Range</th><th>Default</th><th>Example</th></tr>
<tr><td>byte</td><td>1 byte (8 bits)</td><td>-128 to 127</td><td>0</td><td>byte b = 10;</td></tr>
<tr><td>short</td><td>2 bytes</td><td>-32768 to 32767</td><td>0</td><td>short s = 500;</td></tr>
<tr><td>int</td><td>4 bytes</td><td>-2^31 to 2^31-1</td><td>0</td><td>int i = 1000;</td></tr>
<tr><td>long</td><td>8 bytes</td><td>-2^63 to 2^63-1</td><td>0L</td><td>long l = 100L;</td></tr>
<tr><td>float</td><td>4 bytes</td><td>~±3.4×10^38</td><td>0.0f</td><td>float f = 3.14f;</td></tr>
<tr><td>double</td><td>8 bytes</td><td>~±1.8×10^308</td><td>0.0d</td><td>double d = 3.14;</td></tr>
<tr><td>char</td><td>2 bytes</td><td>0 to 65535 (Unicode)</td><td>'\\u0000'</td><td>char c = 'A';</td></tr>
<tr><td>boolean</td><td>1 bit</td><td>true / false</td><td>false</td><td>boolean flag = true;</td></tr>
</table>
"""+info("Java uses <strong>Unicode</strong> for <code>char</code> (2 bytes), unlike C/C++ which uses ASCII (1 byte). This is why Java supports international character sets."))

c2 += sec("📌","Variables","""
<h3>Types of Variables in Java</h3>
<table>
<tr><th>Type</th><th>Declared Inside</th><th>Default Value</th><th>Lifetime</th></tr>
<tr><td>Local Variable</td><td>Method / Block</td><td>No default — must initialize</td><td>Until method exits</td></tr>
<tr><td>Instance Variable</td><td>Class (no static)</td><td>Has default (0, null, false)</td><td>Until object is GC'd</td></tr>
<tr><td>Static Variable</td><td>Class (with static)</td><td>Has default</td><td>Until class is unloaded</td></tr>
</table>
"""+code("""<span class="kw">class</span> <span class="cls">Example</span> {
    <span class="kw">static int</span> count = <span class="num">0</span>;     <span class="cm">// static variable — shared by all objects</span>
    <span class="kw">int</span> id;                    <span class="cm">// instance variable — per object</span>

    <span class="kw">void</span> <span class="fn">show</span>() {
        <span class="kw">int</span> local = <span class="num">10</span>;          <span class="cm">// local variable — must be initialized</span>
        <span class="cls">System</span>.out.println(local);
    }
}""")+warn("Local variables have NO default value. Using an uninitialized local variable causes a compile-time error."))

c2 += sec("➕","Operators","""
<table>
<tr><th>Category</th><th>Operators</th><th>Example</th></tr>
<tr><td>Arithmetic</td><td>+ - * / %</td><td>a + b, a % b</td></tr>
<tr><td>Relational</td><td>== != &lt; &gt; &lt;= &gt;=</td><td>a == b, a &lt; b</td></tr>
<tr><td>Logical</td><td>&amp;&amp; || !</td><td>a&amp;&amp;b, !flag</td></tr>
<tr><td>Bitwise</td><td>&amp; | ^ ~ &lt;&lt; &gt;&gt; &gt;&gt;&gt;</td><td>a &amp; b, a &lt;&lt; 2</td></tr>
<tr><td>Assignment</td><td>= += -= *= /= %=</td><td>a += 5</td></tr>
<tr><td>Ternary</td><td>? :</td><td>max = (a&gt;b) ? a : b</td></tr>
<tr><td>Increment/Decrement</td><td>++ --</td><td>a++, --b</td></tr>
</table>
"""+note("Short-circuit evaluation: In <code>&&</code>, if the left operand is <code>false</code>, the right side is NOT evaluated. In <code>||</code>, if left is <code>true</code>, right is skipped."))

c2 += sec("🔄","Control Structures","""
"""+code("""<span class="cm">// if-else</span>
<span class="kw">if</span> (marks >= <span class="num">60</span>) {
    <span class="cls">System</span>.out.println(<span class="str">"Pass"</span>);
} <span class="kw">else if</span> (marks >= <span class="num">35</span>) {
    <span class="cls">System</span>.out.println(<span class="str">"Compartment"</span>);
} <span class="kw">else</span> {
    <span class="cls">System</span>.out.println(<span class="str">"Fail"</span>);
}

<span class="cm">// switch</span>
<span class="kw">switch</span> (day) {
    <span class="kw">case</span> <span class="num">1</span>: <span class="cls">System</span>.out.println(<span class="str">"Monday"</span>); <span class="kw">break</span>;
    <span class="kw">case</span> <span class="num">2</span>: <span class="cls">System</span>.out.println(<span class="str">"Tuesday"</span>); <span class="kw">break</span>;
    <span class="kw">default</span>: <span class="cls">System</span>.out.println(<span class="str">"Other"</span>);
}

<span class="cm">// for loop</span>
<span class="kw">for</span> (<span class="kw">int</span> i = <span class="num">0</span>; i < <span class="num">5</span>; i++) { <span class="cls">System</span>.out.print(i + <span class="str">" "</span>); }

<span class="cm">// while</span>
<span class="kw">while</span> (n > <span class="num">0</span>) { sum += n % <span class="num">10</span>; n /= <span class="num">10</span>; }

<span class="cm">// do-while (executes at least once)</span>
<span class="kw">do</span> { <span class="cls">System</span>.out.println(<span class="str">"Entered"</span>); } <span class="kw">while</span> (<span class="kw">false</span>);"""))

c2 += sec("📋","Arrays","""
<p>An array is a collection of elements of the <strong>same type</strong> stored in contiguous memory locations.</p>
"""+code("""<span class="cm">// 1D Array</span>
<span class="kw">int</span>[] marks = <span class="kw">new int</span>[<span class="num">5</span>];         <span class="cm">// declaration + creation</span>
<span class="kw">int</span>[] scores = {<span class="num">85</span>, <span class="num">92</span>, <span class="num">78</span>, <span class="num">95</span>, <span class="num">88</span>}; <span class="cm">// declaration + init</span>

<span class="cm">// Enhanced for loop</span>
<span class="kw">for</span> (<span class="kw">int</span> s : scores) {
    <span class="cls">System</span>.out.print(s + <span class="str">" "</span>);
}

<span class="cm">// 2D Array</span>
<span class="kw">int</span>[][] matrix = <span class="kw">new int</span>[<span class="num">3</span>][<span class="num">3</span>];
<span class="kw">int</span>[][] grid = {{<span class="num">1</span>,<span class="num">2</span>,<span class="num">3</span>}, {<span class="num">4</span>,<span class="num">5</span>,<span class="num">6</span>}, {<span class="num">7</span>,<span class="num">8</span>,<span class="num">9</span>}};""")+note("Arrays in Java are objects, not primitives. <code>array.length</code> gives the size. Array index starts at 0."))

c2 += sec("💬","Console I/O","""
"""+code("""<span class="kw">import</span> java.util.Scanner;

<span class="kw">public class</span> <span class="cls">ConsoleDemo</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="cm">// Input using Scanner</span>
        <span class="cls">Scanner</span> sc = <span class="kw">new</span> <span class="cls">Scanner</span>(<span class="cls">System</span>.in);
        <span class="cls">System</span>.out.print(<span class="str">"Enter name: "</span>);
        <span class="cls">String</span> name = sc.nextLine();
        <span class="cls">System</span>.out.print(<span class="str">"Enter age: "</span>);
        <span class="kw">int</span> age = sc.nextInt();

        <span class="cm">// Output</span>
        <span class="cls">System</span>.out.println(<span class="str">"Hello, "</span> + name + <span class="str">"! Age: "</span> + age);
        <span class="cls">System</span>.out.printf(<span class="str">"Formatted: %s is %d years old%n"</span>, name, age);

        sc.close();
    }
}"""))

c2 += body_close("java_w01.html","Week 1&2: OOP Fundamentals","java_w04.html","Week 4&5: Classes & Objects")
with open(f"{BASE}/java_w03.html","w",encoding="utf-8") as f:
    f.write(c2)
print("✅ java_w03.html")

# ═══════════════════════════════════════════════════════
# PAGE 3 — Week 4 & 5: Classes, Objects & Constructors
# ═══════════════════════════════════════════════════════
toc3 = ["Defining a Class","Creating Objects","Constructors","Constructor Overloading","Method Overloading","Parameter Passing","this Keyword (intro)"]
c3 = shell()
c3 += body_open("Week 4 & 5 · CO-1","Classes, Objects & Constructors","co1","CO-1",
    "Classes, Objects, Constructors, Methods, Overloading, Parameter Passing",
    toc3,"java_w03.html","Week 3: Java Language Basics","java_w06.html","Week 6: Static, this, final & Strings")

c3 += sec("🏗️","Defining a Class","""
<p>A class is defined using the <code>class</code> keyword. It is a template containing fields (attributes) and methods (behaviours).</p>
<h3>Anatomy of a Java Class</h3>
"""+code("""<span class="kw">class</span> <span class="cls">Employee</span> {
    <span class="cm">// ── Instance variables ──</span>
    <span class="kw">int</span>    empId;
    <span class="cls">String</span> name;
    <span class="kw">double</span> salary;

    <span class="cm">// ── Constructor ──</span>
    <span class="cls">Employee</span>(<span class="kw">int</span> id, <span class="cls">String</span> n, <span class="kw">double</span> sal) {
        empId  = id;
        name   = n;
        salary = sal;
    }

    <span class="cm">// ── Instance method ──</span>
    <span class="kw">void</span> <span class="fn">display</span>() {
        <span class="cls">System</span>.out.printf(<span class="str">"ID: %d | Name: %s | Salary: %.2f%n"</span>, empId, name, salary);
    }

    <span class="cm">// ── Static method ──</span>
    <span class="kw">static void</span> <span class="fn">companyName</span>() {
        <span class="cls">System</span>.out.println(<span class="str">"ANITS Engineering College"</span>);
    }
}"""))

c3 += sec("🆕","Creating Objects","""
<p>Objects are created using the <code>new</code> keyword. This allocates memory on the heap and calls the constructor.</p>
"""+code("""<span class="kw">public class</span> <span class="cls">Main</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="cm">// Creating objects</span>
        <span class="cls">Employee</span> e1 = <span class="kw">new</span> <span class="cls">Employee</span>(<span class="num">101</span>, <span class="str">"Ravi"</span>, <span class="num">45000.0</span>);
        <span class="cls">Employee</span> e2 = <span class="kw">new</span> <span class="cls">Employee</span>(<span class="num">102</span>, <span class="str">"Priya"</span>, <span class="num">52000.0</span>);

        e1.<span class="fn">display</span>();
        e2.<span class="fn">display</span>();
        <span class="cls">Employee</span>.<span class="fn">companyName</span>(); <span class="cm">// static method via class name</span>
    }
}""")+note("Memory is allocated on the <strong>Heap</strong> for objects. The reference variable (e.g., <code>e1</code>) is stored on the <strong>Stack</strong>."))

c3 += sec("🔧","Constructors","""
<p>A <strong>constructor</strong> is a special method that is automatically called when an object is created. Its purpose is to initialize the object's state.</p>
<h3>Rules for Constructors</h3>
<ul>
<li>Constructor name must be <strong>exactly the same</strong> as the class name</li>
<li>Constructor has <strong>no return type</strong> (not even void)</li>
<li>Constructor is called <strong>automatically</strong> when object is created with <code>new</code></li>
<li>A constructor <strong>can be overloaded</strong></li>
</ul>
<h3>Types of Constructors</h3>
<table>
<tr><th>Type</th><th>Description</th></tr>
<tr><td>Default Constructor</td><td>Provided by JVM if no constructor is defined; initializes fields to defaults</td></tr>
<tr><td>No-Arg Constructor</td><td>Defined by programmer with no parameters</td></tr>
<tr><td>Parameterized Constructor</td><td>Accepts arguments to initialize fields with specific values</td></tr>
</table>
"""+code("""<span class="kw">class</span> <span class="cls">Box</span> {
    <span class="kw">double</span> length, width, height;

    <span class="cm">// No-arg constructor</span>
    <span class="cls">Box</span>() {
        length = width = height = <span class="num">1.0</span>;
    }

    <span class="cm">// Parameterized constructor</span>
    <span class="cls">Box</span>(<span class="kw">double</span> l, <span class="kw">double</span> w, <span class="kw">double</span> h) {
        length = l; width = w; height = h;
    }

    <span class="kw">double</span> <span class="fn">volume</span>() { <span class="kw">return</span> length * width * height; }
}"""))

c3 += sec("🔁","Constructor Overloading","""
<p>Having multiple constructors in the same class with different parameter lists is called <strong>constructor overloading</strong>. It provides flexibility in object creation.</p>
"""+code("""<span class="kw">class</span> <span class="cls">Student</span> {
    <span class="kw">int</span>    rollNo;
    <span class="cls">String</span> name;
    <span class="kw">double</span> cgpa;

    <span class="cls">Student</span>() {                         <span class="cm">// No-arg</span>
        rollNo = <span class="num">0</span>; name = <span class="str">"Unknown"</span>; cgpa = <span class="num">0.0</span>;
    }
    <span class="cls">Student</span>(<span class="kw">int</span> r, <span class="cls">String</span> n) {          <span class="cm">// 2-arg</span>
        rollNo = r; name = n; cgpa = <span class="num">0.0</span>;
    }
    <span class="cls">Student</span>(<span class="kw">int</span> r, <span class="cls">String</span> n, <span class="kw">double</span> g) { <span class="cm">// 3-arg</span>
        rollNo = r; name = n; cgpa = g;
    }
    <span class="kw">void</span> <span class="fn">show</span>() {
        <span class="cls">System</span>.out.printf(<span class="str">"%d | %s | %.2f%n"</span>, rollNo, name, cgpa);
    }
}

<span class="kw">public class</span> <span class="cls">Test</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="kw">new</span> <span class="cls">Student</span>().<span class="fn">show</span>();
        <span class="kw">new</span> <span class="cls">Student</span>(<span class="num">101</span>, <span class="str">"Arjun"</span>).<span class="fn">show</span>();
        <span class="kw">new</span> <span class="cls">Student</span>(<span class="num">102</span>, <span class="str">"Priya"</span>, <span class="num">9.2</span>).<span class="fn">show</span>();
    }
}"""))

c3 += sec("♻️","Method Overloading","""
<p><strong>Method Overloading</strong> = same method name, different parameter list. The compiler differentiates them based on number, type, or order of parameters.</p>
"""+code("""<span class="kw">class</span> <span class="cls">MathUtil</span> {
    <span class="kw">static int</span>    <span class="fn">square</span>(<span class="kw">int</span> n)    { <span class="kw">return</span> n * n; }
    <span class="kw">static double</span> <span class="fn">square</span>(<span class="kw">double</span> n) { <span class="kw">return</span> n * n; }

    <span class="kw">static int</span>    <span class="fn">add</span>(<span class="kw">int</span> a, <span class="kw">int</span> b)          { <span class="kw">return</span> a + b; }
    <span class="kw">static int</span>    <span class="fn">add</span>(<span class="kw">int</span> a, <span class="kw">int</span> b, <span class="kw">int</span> c)    { <span class="kw">return</span> a + b + c; }
    <span class="kw">static double</span> <span class="fn">add</span>(<span class="kw">double</span> a, <span class="kw">double</span> b)    { <span class="kw">return</span> a + b; }
}""")+warn("Method overloading is <strong>compile-time polymorphism</strong>. Return type alone cannot distinguish overloaded methods — the compiler will throw an error."))

c3 += sec("📨","Parameter Passing","""
<p>Java always uses <strong>Pass by Value</strong>.</p>
<ul>
<li>For <strong>primitives</strong>: a copy of the value is passed — changes inside the method do NOT affect the original.</li>
<li>For <strong>objects</strong>: the <em>reference</em> (address) is passed by value — changes to the object's fields inside the method DO affect the original object, but reassigning the reference does not.</li>
</ul>
"""+code("""<span class="kw">void</span> <span class="fn">changeVal</span>(<span class="kw">int</span> x) { x = <span class="num">100</span>; }      <span class="cm">// original unchanged</span>
<span class="kw">void</span> <span class="fn">changeObj</span>(<span class="cls">Box</span> b) { b.length = <span class="num">99</span>; } <span class="cm">// original object IS changed</span>"""))

c3 += sec("🔑","this Keyword (intro)","""
<p>The <code>this</code> keyword refers to the <strong>current object</strong>. Use it when a local variable shadows an instance variable:</p>
"""+code("""<span class="kw">class</span> <span class="cls">Circle</span> {
    <span class="kw">double</span> radius;

    <span class="cls">Circle</span>(<span class="kw">double</span> radius) {
        <span class="kw">this</span>.radius = radius; <span class="cm">// 'this.radius' = instance var, 'radius' = param</span>
    }
    <span class="kw">double</span> <span class="fn">area</span>() { <span class="kw">return</span> Math.PI * <span class="kw">this</span>.radius * <span class="kw">this</span>.radius; }
}""")+note("<code>this()</code> can also be used to call one constructor from another (constructor chaining). It must be the first statement in the constructor."))

c3 += body_close("java_w03.html","Week 3: Java Language Basics","java_w06.html","Week 6: Static, this, final & Strings")
with open(f"{BASE}/java_w04.html","w",encoding="utf-8") as f:
    f.write(c3)
print("✅ java_w04.html")

# ═══════════════════════════════════════════════════════
# PAGE 4 — Week 6: Static, this, final & String Handling
# ═══════════════════════════════════════════════════════
toc4 = ["Static Members","Static Block","this Reference","final Keyword","String Class","StringBuffer & StringBuilder","StringTokenizer"]
c4 = shell()
c4 += body_open("Week 6 · CO-1","Static, this, final & String Handling","co1","CO-1",
    "Static fields/methods/blocks, this reference, final keyword, String handling",
    toc4,"java_w04.html","Week 4&5: Classes & Objects","java_w07.html","Week 7: Inheritance & Polymorphism")

c4 += sec("⚡","Static Members","""
<p>The <code>static</code> keyword belongs to the <strong>class</strong> rather than to any instance. Static members are shared across all objects of a class.</p>
<table>
<tr><th>Feature</th><th>Static</th><th>Non-Static (Instance)</th></tr>
<tr><td>Memory</td><td>Allocated once (class load)</td><td>Allocated per object</td></tr>
<tr><td>Access</td><td>ClassName.member</td><td>objectRef.member</td></tr>
<tr><td>Can access</td><td>Only static members directly</td><td>Both static and instance</td></tr>
<tr><td>Example</td><td>Math.PI, Math.sqrt()</td><td>obj.length, obj.getArea()</td></tr>
</table>
"""+code("""<span class="kw">class</span> <span class="cls">Counter</span> {
    <span class="kw">static int</span> count = <span class="num">0</span>; <span class="cm">// shared by all objects</span>
    <span class="kw">int</span> id;

    <span class="cls">Counter</span>() {
        count++;
        id = count;
    }

    <span class="kw">static void</span> <span class="fn">showCount</span>() {
        <span class="cm">// can NOT access 'id' here — id is instance variable</span>
        <span class="cls">System</span>.out.println(<span class="str">"Total objects: "</span> + count);
    }
}

<span class="cls">Counter</span> c1 = <span class="kw">new</span> <span class="cls">Counter</span>();
<span class="cls">Counter</span> c2 = <span class="kw">new</span> <span class="cls">Counter</span>();
<span class="cls">Counter</span>.<span class="fn">showCount</span>(); <span class="cm">// Output: Total objects: 2</span>"""))

c4 += sec("🔲","Static Block","""
<p>A <strong>static block</strong> is executed <em>once</em>, when the class is first loaded into memory — before the <code>main()</code> method runs. Used for complex static initializations.</p>
"""+code("""<span class="kw">class</span> <span class="cls">Config</span> {
    <span class="kw">static</span> <span class="cls">String</span> dbUrl;
    <span class="kw">static int</span> port;

    <span class="kw">static</span> {  <span class="cm">// runs once at class load time</span>
        dbUrl = <span class="str">"jdbc:mysql://localhost/college"</span>;
        port  = <span class="num">3306</span>;
        <span class="cls">System</span>.out.println(<span class="str">"Config loaded."</span>);
    }
}"""))

c4 += sec("🔑","this Reference","""
<p>The <code>this</code> keyword refers to the <strong>current class instance</strong>. Its four main uses:</p>
<ol>
<li>Differentiate instance variable from local variable with the same name</li>
<li>Pass the current object as an argument to a method</li>
<li>Return the current object from a method (method chaining)</li>
<li>Call another constructor in the same class using <code>this()</code></li>
</ol>
"""+code("""<span class="kw">class</span> <span class="cls">Builder</span> {
    <span class="kw">int</span> x, y;

    <span class="cls">Builder</span> <span class="fn">setX</span>(<span class="kw">int</span> x) { <span class="kw">this</span>.x = x; <span class="kw">return this</span>; } <span class="cm">// method chaining</span>
    <span class="cls">Builder</span> <span class="fn">setY</span>(<span class="kw">int</span> y) { <span class="kw">this</span>.y = y; <span class="kw">return this</span>; }

    <span class="cls">Builder</span>(<span class="kw">int</span> x) {
        <span class="kw">this</span>(x, <span class="num">0</span>); <span class="cm">// calls Builder(int,int) — must be first line</span>
    }
    <span class="cls">Builder</span>(<span class="kw">int</span> x, <span class="kw">int</span> y) { <span class="kw">this</span>.x = x; <span class="kw">this</span>.y = y; }
}

<span class="cm">// Method chaining usage</span>
<span class="cls">Builder</span> b = <span class="kw">new</span> <span class="cls">Builder</span>(<span class="num">0</span>).<span class="fn">setX</span>(<span class="num">10</span>).<span class="fn">setY</span>(<span class="num">20</span>);"""))

c4 += sec("🔒","final Keyword","""
<p>The <code>final</code> keyword restricts further modification.</p>
<table>
<tr><th>Applied To</th><th>Effect</th></tr>
<tr><td>Variable</td><td>Becomes a constant — cannot be reassigned</td></tr>
<tr><td>Method</td><td>Cannot be overridden in subclass</td></tr>
<tr><td>Class</td><td>Cannot be extended (inherited)</td></tr>
</table>
"""+code("""<span class="kw">final class</span> <span class="cls">Immutable</span> {         <span class="cm">// cannot be subclassed</span>
    <span class="kw">final double</span> PI = <span class="num">3.14159</span>;    <span class="cm">// constant</span>

    <span class="kw">final void</span> <span class="fn">show</span>() {            <span class="cm">// cannot be overridden</span>
        <span class="cls">System</span>.out.println(<span class="str">"PI = "</span> + PI);
    }
}""")+note("The <code>String</code> class in Java is declared <code>final</code> — you cannot extend String. This is why String is immutable."))

c4 += sec("📝","String Class","""
<p>Strings in Java are <strong>immutable objects</strong> of the <code>java.lang.String</code> class. Once created, their value cannot be changed.</p>
<h3>Important String Methods</h3>
<table>
<tr><th>Method</th><th>Description</th><th>Example</th></tr>
<tr><td>length()</td><td>Returns string length</td><td>"Java".length() → 4</td></tr>
<tr><td>charAt(i)</td><td>Returns char at index i</td><td>"Java".charAt(1) → 'a'</td></tr>
<tr><td>substring(s,e)</td><td>Extracts [s,e)</td><td>"Hello".substring(1,4) → "ell"</td></tr>
<tr><td>indexOf(str)</td><td>First occurrence index</td><td>"Hello".indexOf("l") → 2</td></tr>
<tr><td>toUpperCase()</td><td>Converts to uppercase</td><td>"java".toUpperCase() → "JAVA"</td></tr>
<tr><td>toLowerCase()</td><td>Converts to lowercase</td><td>"JAVA".toLowerCase() → "java"</td></tr>
<tr><td>trim()</td><td>Removes leading/trailing spaces</td><td>"  hi  ".trim() → "hi"</td></tr>
<tr><td>replace(o,n)</td><td>Replace all occurrences</td><td>"aaa".replace('a','b') → "bbb"</td></tr>
<tr><td>equals(s)</td><td>Content comparison</td><td>"hi".equals("hi") → true</td></tr>
<tr><td>equalsIgnoreCase(s)</td><td>Case-insensitive compare</td><td>"Hi".equalsIgnoreCase("hi") → true</td></tr>
<tr><td>split(regex)</td><td>Splits into array</td><td>"a,b,c".split(",") → ["a","b","c"]</td></tr>
<tr><td>contains(s)</td><td>Checks if substring present</td><td>"Hello".contains("ell") → true</td></tr>
<tr><td>startsWith(s)</td><td>Checks prefix</td><td>"Java".startsWith("Ja") → true</td></tr>
</table>
"""+warn("Never compare strings with <code>==</code>. Use <code>.equals()</code>. The <code>==</code> operator compares references (memory addresses), not content."))

c4 += sec("⚡","StringBuffer & StringBuilder","""
<table>
<tr><th>Feature</th><th>String</th><th>StringBuffer</th><th>StringBuilder</th></tr>
<tr><td>Mutable</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Thread-safe</td><td>Yes (immutable)</td><td>Yes (synchronized)</td><td>No</td></tr>
<tr><td>Performance</td><td>Slow (creates new object)</td><td>Moderate</td><td>Fastest</td></tr>
<tr><td>Use when</td><td>Fixed strings</td><td>Multi-threaded env</td><td>Single-threaded</td></tr>
</table>
"""+code("""<span class="cls">StringBuilder</span> sb = <span class="kw">new</span> <span class="cls">StringBuilder</span>(<span class="str">"Hello"</span>);
sb.<span class="fn">append</span>(<span class="str">" World"</span>);   <span class="cm">// Hello World</span>
sb.<span class="fn">insert</span>(<span class="num">5</span>, <span class="str">","</span>);      <span class="cm">// Hello, World</span>
sb.<span class="fn">reverse</span>();            <span class="cm">// dlroW ,olleH</span>
sb.<span class="fn">delete</span>(<span class="num">0</span>, <span class="num">6</span>);        <span class="cm">// ,olleH</span>
sb.<span class="fn">replace</span>(<span class="num">0</span>, <span class="num">1</span>, <span class="str">"!"</span>);  <span class="cm">// !olleH</span>
<span class="cls">System</span>.out.println(sb.<span class="fn">toString</span>());"""))

c4 += sec("✂️","StringTokenizer","""
<p><code>StringTokenizer</code> (in <code>java.util</code>) splits a string into tokens based on a delimiter.</p>
"""+code("""<span class="kw">import</span> java.util.StringTokenizer;

<span class="cls">String</span> csv = <span class="str">"Ravi,22,Computer Science,9.1"</span>;
<span class="cls">StringTokenizer</span> st = <span class="kw">new</span> <span class="cls">StringTokenizer</span>(csv, <span class="str">","</span>);

<span class="kw">while</span> (st.<span class="fn">hasMoreTokens</span>()) {
    <span class="cls">System</span>.out.println(st.<span class="fn">nextToken</span>());
}
<span class="cm">// Output: Ravi  22  Computer Science  9.1</span>"""))

c4 += body_close("java_w04.html","Week 4&5: Classes & Objects","java_w07.html","Week 7: Inheritance & Polymorphism")
with open(f"{BASE}/java_w06.html","w",encoding="utf-8") as f:
    f.write(c4)
print("✅ java_w06.html")

# ═══════════════════════════════════════════════════════
# PAGE 5 — Week 7: Inheritance & Polymorphism
# ═══════════════════════════════════════════════════════
toc5 = ["Inheritance Overview","Types of Inheritance","super Keyword","Method Overriding","final with Inheritance","Abstract Classes","Runtime Polymorphism"]
c5 = shell()
c5 += body_open("Week 7 · CO-1","Inheritance & Polymorphism","co1","CO-1",
    "Types of Inheritance, super, Method Overriding, Abstract Classes, Dynamic Dispatch",
    toc5,"java_w06.html","Week 6: Static, this, final & Strings","java_w08.html","Week 8: Interfaces")

c5 += sec("🔗","Inheritance Overview","""
<p><strong>Inheritance</strong> enables one class to inherit fields and methods from another. It supports <strong>code reusability</strong> and establishes an IS-A relationship.</p>
<ul>
<li>Parent class → <strong>Super class / Base class</strong></li>
<li>Child class → <strong>Sub class / Derived class</strong></li>
<li>Keyword: <code>extends</code></li>
</ul>
"""+note("Java does <strong>not</strong> support multiple inheritance through classes (to avoid the Diamond Problem), but it IS supported through interfaces."))

c5 += sec("🌳","Types of Inheritance","""
<table>
<tr><th>Type</th><th>Description</th><th>Java Support</th></tr>
<tr><td>Single</td><td>One child inherits one parent</td><td>✅ Yes</td></tr>
<tr><td>Multi-level</td><td>A→B→C (chain)</td><td>✅ Yes</td></tr>
<tr><td>Hierarchical</td><td>One parent, multiple children</td><td>✅ Yes</td></tr>
<tr><td>Multiple</td><td>One child, multiple parents</td><td>❌ Via classes — ✅ Via interfaces</td></tr>
<tr><td>Hybrid</td><td>Combination of above</td><td>✅ Via interfaces</td></tr>
</table>
"""+code("""<span class="cm">// Multi-level inheritance</span>
<span class="kw">class</span> <span class="cls">Animal</span>   { <span class="kw">void</span> <span class="fn">breathe</span>() { <span class="cls">System</span>.out.println(<span class="str">"Breathes"</span>); } }
<span class="kw">class</span> <span class="cls">Mammal</span>   <span class="kw">extends</span> <span class="cls">Animal</span>  { <span class="kw">void</span> <span class="fn">walk</span>()    { <span class="cls">System</span>.out.println(<span class="str">"Walks"</span>); } }
<span class="kw">class</span> <span class="cls">Dog</span>      <span class="kw">extends</span> <span class="cls">Mammal</span>  { <span class="kw">void</span> <span class="fn">bark</span>()    { <span class="cls">System</span>.out.println(<span class="str">"Barks"</span>); } }

<span class="cls">Dog</span> d = <span class="kw">new</span> <span class="cls">Dog</span>();
d.<span class="fn">breathe</span>(); d.<span class="fn">walk</span>(); d.<span class="fn">bark</span>(); <span class="cm">// all three accessible</span>"""))

c5 += sec("⬆️","super Keyword","""
<p>The <code>super</code> keyword refers to the <strong>immediate parent class</strong>. It is used to:</p>
<ol>
<li>Access parent class fields (when shadowed by child)</li>
<li>Call parent class methods (especially overridden ones)</li>
<li>Call parent class constructor — <code>super()</code> must be first line</li>
</ol>
"""+code("""<span class="kw">class</span> <span class="cls">Shape</span> {
    <span class="cls">String</span> color;
    <span class="cls">Shape</span>(<span class="cls">String</span> color) { <span class="kw">this</span>.color = color; }
    <span class="kw">void</span> <span class="fn">draw</span>() { <span class="cls">System</span>.out.println(<span class="str">"Drawing "</span> + color + <span class="str">" shape"</span>); }
}

<span class="kw">class</span> <span class="cls">Rectangle</span> <span class="kw">extends</span> <span class="cls">Shape</span> {
    <span class="kw">double</span> width, height;

    <span class="cls">Rectangle</span>(<span class="cls">String</span> color, <span class="kw">double</span> w, <span class="kw">double</span> h) {
        <span class="kw">super</span>(color);      <span class="cm">// call parent constructor</span>
        width = w; height = h;
    }

    <span class="kw">void</span> <span class="fn">draw</span>() {
        <span class="kw">super</span>.<span class="fn">draw</span>();       <span class="cm">// call parent method</span>
        <span class="cls">System</span>.out.println(<span class="str">"Rectangle: "</span> + width + <span class="str">"x"</span> + height);
    }
}"""))

c5 += sec("🔄","Method Overriding","""
<p><strong>Method Overriding</strong> occurs when a subclass provides its own implementation of a method already defined in the parent class. Rules:</p>
<ul>
<li>Same method name, same parameter list, same or covariant return type</li>
<li>Access modifier can be same or wider (not more restrictive)</li>
<li>Cannot override <code>static</code>, <code>final</code>, or <code>private</code> methods</li>
<li>Use <code>@Override</code> annotation for compile-time safety</li>
</ul>
"""+code("""<span class="kw">class</span> <span class="cls">Bank</span> {
    <span class="kw">double</span> <span class="fn">getInterestRate</span>() { <span class="kw">return</span> <span class="num">4.0</span>; }
}
<span class="kw">class</span> <span class="cls">SBI</span> <span class="kw">extends</span> <span class="cls">Bank</span> {
    <span class="ann">@Override</span>
    <span class="kw">double</span> <span class="fn">getInterestRate</span>() { <span class="kw">return</span> <span class="num">7.0</span>; }
}
<span class="kw">class</span> <span class="cls">HDFC</span> <span class="kw">extends</span> <span class="cls">Bank</span> {
    <span class="ann">@Override</span>
    <span class="kw">double</span> <span class="fn">getInterestRate</span>() { <span class="kw">return</span> <span class="num">6.5</span>; }
}"""))

c5 += sec("🚫","final with Inheritance","""
<table>
<tr><th>Usage</th><th>Effect</th></tr>
<tr><td><code>final class</code></td><td>Class cannot be extended at all</td></tr>
<tr><td><code>final method</code></td><td>Method cannot be overridden in subclass</td></tr>
<tr><td><code>final variable</code></td><td>Acts as a constant; cannot be changed</td></tr>
</table>
"""+info("The <code>String</code>, <code>Integer</code>, and other wrapper classes are all declared <code>final</code> in Java's standard library."))

c5 += sec("🎭","Abstract Classes","""
<p>An <strong>abstract class</strong> is a class that cannot be instantiated. It serves as a template, defining methods that subclasses must implement.</p>
<ul>
<li>Declared with the <code>abstract</code> keyword</li>
<li>Can have both abstract (no body) and concrete (with body) methods</li>
<li>If a class has even one abstract method, the class must also be abstract</li>
<li>Subclass must override ALL abstract methods, or itself be abstract</li>
</ul>
"""+code("""<span class="kw">abstract class</span> <span class="cls">Vehicle</span> {
    <span class="kw">int</span> speed;

    <span class="cm">// abstract method — no body</span>
    <span class="kw">abstract void</span> <span class="fn">fuelType</span>();

    <span class="cm">// concrete method</span>
    <span class="kw">void</span> <span class="fn">showSpeed</span>() { <span class="cls">System</span>.out.println(<span class="str">"Speed: "</span> + speed); }
}

<span class="kw">class</span> <span class="cls">Car</span> <span class="kw">extends</span> <span class="cls">Vehicle</span> {
    <span class="ann">@Override</span>
    <span class="kw">void</span> <span class="fn">fuelType</span>() { <span class="cls">System</span>.out.println(<span class="str">"Petrol / Diesel"</span>); }
}

<span class="kw">class</span> <span class="cls">ElectricCar</span> <span class="kw">extends</span> <span class="cls">Vehicle</span> {
    <span class="ann">@Override</span>
    <span class="kw">void</span> <span class="fn">fuelType</span>() { <span class="cls">System</span>.out.println(<span class="str">"Electric Battery"</span>); }
}"""))

c5 += sec("🚀","Runtime Polymorphism","""
<p><strong>Dynamic Method Dispatch</strong> is the mechanism by which an overridden method is called through a parent class reference at runtime. The JVM determines which version to call based on the actual object type — not the reference type.</p>
"""+code("""<span class="kw">public class</span> <span class="cls">Test</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="cls">Bank</span> b;            <span class="cm">// parent reference</span>

        b = <span class="kw">new</span> <span class="cls">SBI</span>();
        <span class="cls">System</span>.out.println(<span class="str">"SBI rate: "</span>  + b.<span class="fn">getInterestRate</span>()); <span class="cm">// 7.0</span>

        b = <span class="kw">new</span> <span class="cls">HDFC</span>();
        <span class="cls">System</span>.out.println(<span class="str">"HDFC rate: "</span> + b.<span class="fn">getInterestRate</span>()); <span class="cm">// 6.5</span>

        <span class="cm">// Array of Bank references → different objects</span>
        <span class="cls">Bank</span>[] banks = { <span class="kw">new</span> <span class="cls">SBI</span>(), <span class="kw">new</span> <span class="cls">HDFC</span>(), <span class="kw">new</span> <span class="cls">Bank</span>() };
        <span class="kw">for</span> (<span class="cls">Bank</span> bank : banks)
            <span class="cls">System</span>.out.println(bank.<span class="fn">getInterestRate</span>()); <span class="cm">// 7.0, 6.5, 4.0</span>
    }
}""")+note("Runtime polymorphism is one of the most powerful OOP features. It lets you write generic code that works with any subclass — the correct version is chosen automatically at runtime."))

c5 += body_close("java_w06.html","Week 6: Static, this, final & Strings","java_w08.html","Week 8: Interfaces")
with open(f"{BASE}/java_w07.html","w",encoding="utf-8") as f:
    f.write(c5)
print("✅ java_w07.html")

# ═══════════════════════════════════════════════════════
# PAGE 6 — Week 8: Interfaces
# ═══════════════════════════════════════════════════════
toc6 = ["What is an Interface?","Defining & Implementing","Interface Reference","Extending Interfaces","Default & Static Methods","Abstract Class vs Interface"]
c6 = shell()
c6 += body_open("Week 8 · CO-2","Interfaces","co2","CO-2",
    "Defining, Implementing, Accessing, Extending Interfaces; Default & Static Methods",
    toc6,"java_w07.html","Week 7: Inheritance & Polymorphism","java_w09.html","Week 9: Packages")

c6 += sec("❓","What is an Interface?","""
<p>An <strong>interface</strong> is a 100% abstract type (in traditional Java) that defines a contract — a set of methods that a class <em>must</em> implement. Interfaces support:</p>
<ul>
<li><strong>Multiple inheritance</strong> — a class can implement many interfaces</li>
<li><strong>Full abstraction</strong> — all methods are abstract by default (before Java 8)</li>
<li><strong>Loose coupling</strong> — code depends on interfaces, not implementations</li>
</ul>
<table>
<tr><th>Interface members (pre-Java 8)</th><th>Default nature</th></tr>
<tr><td>Variables</td><td>public static final (constants)</td></tr>
<tr><td>Methods</td><td>public abstract</td></tr>
</table>
""")

c6 += sec("📐","Defining & Implementing","""
"""+code("""<span class="cm">// Defining an interface</span>
<span class="kw">interface</span> <span class="cls">Drawable</span> {
    <span class="kw">double</span> PI = <span class="num">3.14159</span>;     <span class="cm">// implicitly public static final</span>
    <span class="kw">void</span> <span class="fn">draw</span>();              <span class="cm">// implicitly public abstract</span>
    <span class="kw">double</span> <span class="fn">area</span>();
}

<span class="cm">// Implementing the interface</span>
<span class="kw">class</span> <span class="cls">Circle</span> <span class="kw">implements</span> <span class="cls">Drawable</span> {
    <span class="kw">double</span> r;
    <span class="cls">Circle</span>(<span class="kw">double</span> r) { <span class="kw">this</span>.r = r; }

    <span class="ann">@Override</span>
    <span class="kw">public void</span> <span class="fn">draw</span>()   { <span class="cls">System</span>.out.println(<span class="str">"Drawing circle"</span>); }

    <span class="ann">@Override</span>
    <span class="kw">public double</span> <span class="fn">area</span>() { <span class="kw">return</span> PI * r * r; }
}

<span class="cm">// Implementing multiple interfaces</span>
<span class="kw">interface</span> <span class="cls">Resizable</span> { <span class="kw">void</span> <span class="fn">resize</span>(<span class="kw">double</span> factor); }

<span class="kw">class</span> <span class="cls">Square</span> <span class="kw">implements</span> <span class="cls">Drawable</span>, <span class="cls">Resizable</span> {
    <span class="kw">double</span> side;
    <span class="ann">@Override</span> <span class="kw">public void</span>   <span class="fn">draw</span>()              { <span class="cls">System</span>.out.println(<span class="str">"Drawing square"</span>); }
    <span class="ann">@Override</span> <span class="kw">public double</span> <span class="fn">area</span>()              { <span class="kw">return</span> side * side; }
    <span class="ann">@Override</span> <span class="kw">public void</span>   <span class="fn">resize</span>(<span class="kw">double</span> f)   { side *= f; }
}"""))

c6 += sec("🔗","Interface Reference","""
<p>Just like abstract classes, an interface reference can hold any object that implements it.</p>
"""+code("""<span class="cls">Drawable</span> d;

d = <span class="kw">new</span> <span class="cls">Circle</span>(<span class="num">5.0</span>);
d.<span class="fn">draw</span>();                         <span class="cm">// Circle's draw</span>
<span class="cls">System</span>.out.println(d.<span class="fn">area</span>());    <span class="cm">// Circle's area — runtime dispatch</span>

d = <span class="kw">new</span> <span class="cls">Square</span>();
d.<span class="fn">draw</span>();                         <span class="cm">// Square's draw</span>""")+note("Interface references enable runtime polymorphism and are the foundation of programming to abstractions (Dependency Inversion Principle)."))

c6 += sec("🔀","Extending Interfaces","""
<p>An interface can extend one or more other interfaces using <code>extends</code>.</p>
"""+code("""<span class="kw">interface</span> <span class="cls">Shape</span>   { <span class="kw">double</span> <span class="fn">area</span>(); }
<span class="kw">interface</span> <span class="cls">Shape3D</span> <span class="kw">extends</span> <span class="cls">Shape</span> {
    <span class="kw">double</span> <span class="fn">volume</span>();
}

<span class="cm">// extending multiple interfaces</span>
<span class="kw">interface</span> <span class="cls">Printable</span>  { <span class="kw">void</span> <span class="fn">print</span>(); }
<span class="kw">interface</span> <span class="cls">Saveable</span>   { <span class="kw">void</span> <span class="fn">save</span>(); }
<span class="kw">interface</span> <span class="cls">Document</span> <span class="kw">extends</span> <span class="cls">Printable</span>, <span class="cls">Saveable</span> {
    <span class="kw">void</span> <span class="fn">open</span>();
}"""))

c6 += sec("🆕","Default & Static Methods (Java 8+)","""
<p>Java 8 added <code>default</code> and <code>static</code> methods to interfaces, allowing backward-compatible evolution of APIs.</p>
<table>
<tr><th>Type</th><th>Keyword</th><th>Called via</th><th>Can be overridden</th></tr>
<tr><td>Default method</td><td>default</td><td>Object reference</td><td>Yes (in implementing class)</td></tr>
<tr><td>Static method</td><td>static</td><td>InterfaceName.method()</td><td>No</td></tr>
</table>
"""+code("""<span class="kw">interface</span> <span class="cls">Logger</span> {
    <span class="kw">void</span> <span class="fn">log</span>(<span class="cls">String</span> msg);   <span class="cm">// abstract — must implement</span>

    <span class="kw">default void</span> <span class="fn">logInfo</span>(<span class="cls">String</span> msg) {   <span class="cm">// default — optional to override</span>
        <span class="fn">log</span>(<span class="str">"[INFO] "</span> + msg);
    }

    <span class="kw">static</span> <span class="cls">Logger</span> <span class="fn">console</span>() {             <span class="cm">// static factory method</span>
        <span class="kw">return</span> msg -> <span class="cls">System</span>.out.println(msg);
    }
}"""))

c6 += sec("⚖️","Abstract Class vs Interface","""
<table>
<tr><th>Feature</th><th>Abstract Class</th><th>Interface</th></tr>
<tr><td>Keyword</td><td>abstract class</td><td>interface</td></tr>
<tr><td>Multiple inheritance</td><td>❌ No</td><td>✅ Yes</td></tr>
<tr><td>Constructors</td><td>✅ Yes</td><td>❌ No</td></tr>
<tr><td>Fields</td><td>Any type</td><td>public static final only</td></tr>
<tr><td>Methods</td><td>Any (abstract + concrete)</td><td>abstract, default, static</td></tr>
<tr><td>Access modifiers</td><td>Any</td><td>All public by default</td></tr>
<tr><td>Use when</td><td>Shared base code + partial abstraction</td><td>Full contract; multiple inheritance</td></tr>
</table>
"""+note("Rule of thumb: Use an <strong>interface</strong> when you need to define a contract (what to do). Use an <strong>abstract class</strong> when you need to share code (how to partly do it)."))

c6 += body_close("java_w07.html","Week 7: Inheritance & Polymorphism","java_w09.html","Week 9: Packages")
with open(f"{BASE}/java_w08.html","w",encoding="utf-8") as f:
    f.write(c6)
print("✅ java_w08.html")

# PAGE 7 — Week 9: Packages
toc7 = ["What is a Package?","Creating Packages","Importing Packages","Access Modifiers","Built-in Packages","Static Import"]
c7 = shell()
c7 += body_open("Week 9 · CO-2","Packages","co2","CO-2",
    "Defining, Creating, Accessing, and Importing Java Packages",
    toc7,"java_w08.html","Week 8: Interfaces","java_w10.html","Week 10: I/O Streams")

c7 += sec("📦","What is a Package?","""
<p>A <strong>package</strong> is a namespace that organises a set of related classes and interfaces — similar to a folder on your file system. Packages prevent naming conflicts and provide access control.</p>
<h3>Benefits</h3>
<ul>
<li>Avoids naming conflicts (two classes can have same name in different packages)</li>
<li>Provides access protection</li>
<li>Makes code easier to locate and maintain</li>
</ul>
<h3>Types of Packages</h3>
<table>
<tr><th>Type</th><th>Description</th><th>Examples</th></tr>
<tr><td>Built-in</td><td>Provided by Java SDK</td><td>java.lang, java.util, java.io</td></tr>
<tr><td>User-defined</td><td>Created by the programmer</td><td>com.college, in.anits.cse</td></tr>
</table>
""")

c7 += sec("🗂️","Creating Packages","""
<p>The <code>package</code> statement must be the <strong>first line</strong> in a Java source file (before any imports or class declarations).</p>
"""+code("""<span class="cm">// File: in/anits/cse/Student.java</span>
<span class="kw">package</span> in.anits.cse;

<span class="kw">public class</span> <span class="cls">Student</span> {
    <span class="kw">private int</span>    rollNo;
    <span class="kw">private</span> <span class="cls">String</span> name;

    <span class="kw">public</span> <span class="cls">Student</span>(<span class="kw">int</span> r, <span class="cls">String</span> n) { rollNo = r; name = n; }

    <span class="kw">public void</span> <span class="fn">show</span>() {
        <span class="cls">System</span>.out.println(<span class="str">"Roll: "</span> + rollNo + <span class="str">" | Name: "</span> + name);
    }
}""")+code("""<span class="cm"># Compile with package structure</span>
javac -d . in/anits/cse/Student.java

<span class="cm"># This creates:  ./in/anits/cse/Student.class</span>
<span class="cm"># Run:</span>
java in.anits.cse.Student"""))

c7 += sec("📥","Importing Packages","""
<table>
<tr><th>Import style</th><th>Example</th><th>What it imports</th></tr>
<tr><td>Fully qualified name</td><td>java.util.Scanner sc = ...</td><td>Single class, no import needed</td></tr>
<tr><td>Single type import</td><td>import java.util.Scanner;</td><td>Only Scanner class</td></tr>
<tr><td>On-demand import</td><td>import java.util.*;</td><td>All classes in java.util (NOT sub-packages)</td></tr>
<tr><td>Static import</td><td>import static java.lang.Math.*;</td><td>All static members of Math</td></tr>
</table>
"""+code("""<span class="kw">import</span> java.util.Scanner;
<span class="kw">import</span> java.util.ArrayList;
<span class="kw">import</span> in.anits.cse.Student;

<span class="kw">public class</span> <span class="cls">Main</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="cls">Student</span> s = <span class="kw">new</span> <span class="cls">Student</span>(<span class="num">101</span>, <span class="str">"Arjun"</span>);
        s.<span class="fn">show</span>();
    }
}""")+warn("'import java.util.*' does NOT import sub-packages. For example, it does not import java.util.concurrent.* — you must import sub-packages separately."))

c7 += sec("🔐","Access Modifiers","""
<table>
<tr><th>Modifier</th><th>Same Class</th><th>Same Package</th><th>Subclass</th><th>Other Package</th></tr>
<tr><td>private</td><td>✅</td><td>❌</td><td>❌</td><td>❌</td></tr>
<tr><td>(default)</td><td>✅</td><td>✅</td><td>❌</td><td>❌</td></tr>
<tr><td>protected</td><td>✅</td><td>✅</td><td>✅</td><td>❌</td></tr>
<tr><td>public</td><td>✅</td><td>✅</td><td>✅</td><td>✅</td></tr>
</table>
"""+note("Use <code>private</code> for data members (encapsulation), <code>public</code> for API methods, and <code>protected</code> for methods intended to be overridden by subclasses."))

c7 += sec("🏛️","Built-in Packages","""
<table>
<tr><th>Package</th><th>Contents</th></tr>
<tr><td>java.lang</td><td>Auto-imported; String, Math, System, Integer, Thread, Object...</td></tr>
<tr><td>java.util</td><td>Scanner, ArrayList, HashMap, Collections, Date...</td></tr>
<tr><td>java.io</td><td>File, FileReader, BufferedReader, FileWriter, InputStream...</td></tr>
<tr><td>java.net</td><td>Socket, URL, HttpURLConnection, InetAddress...</td></tr>
<tr><td>java.sql</td><td>Connection, DriverManager, ResultSet, PreparedStatement...</td></tr>
<tr><td>java.awt</td><td>GUI components: Button, Frame, Panel, Graphics...</td></tr>
<tr><td>javax.swing</td><td>Modern GUI: JFrame, JButton, JLabel, JTable...</td></tr>
</table>
""")

c7 += sec("⚡","Static Import","""
<p>Static import allows you to use static members of a class directly without the class prefix.</p>
"""+code("""<span class="kw">import static</span> java.lang.Math.*;
<span class="kw">import static</span> java.lang.System.out;

<span class="kw">public class</span> <span class="cls">MathDemo</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="cm">// Without static import: Math.sqrt(16), System.out.println</span>
        out.println(<span class="fn">sqrt</span>(<span class="num">16</span>));   <span class="cm">// 4.0</span>
        out.println(<span class="fn">pow</span>(<span class="num">2</span>, <span class="num">10</span>)); <span class="cm">// 1024.0</span>
        out.println(PI);         <span class="cm">// 3.141592653589793</span>
    }
}"""))

c7 += body_close("java_w08.html","Week 8: Interfaces","java_w10.html","Week 10: I/O Streams")
with open(f"{BASE}/java_w09.html","w",encoding="utf-8") as f: f.write(c7)
print("✅ java_w09.html")

# PAGE 8 — Week 10: I/O Streams
toc8 = ["Streams Overview","Byte Streams","Character Streams","FileReader & FileWriter","BufferedReader & BufferedWriter","File Class","Scanner for File Input"]
c8 = shell()
c8 += body_open("Week 10 · CO-2","I/O Streams","co2","CO-2",
    "Reading and Writing Files using Byte and Character Streams",
    toc8,"java_w09.html","Week 9: Packages","java_w11.html","Week 11: Exception Handling")

c8 += sec("🌊","Streams Overview","""
<p>Java I/O is based on <strong>streams</strong> — a sequence of data flowing from a source to a destination. All I/O classes are in the <code>java.io</code> package.</p>
<table>
<tr><th>Category</th><th>Data Unit</th><th>Base Classes</th><th>Class Names End With</th></tr>
<tr><td>Byte Stream</td><td>1 byte (8 bits)</td><td>InputStream, OutputStream</td><td>...Stream</td></tr>
<tr><td>Character Stream</td><td>2 bytes (Unicode)</td><td>Reader, Writer</td><td>...Reader / ...Writer</td></tr>
</table>
"""+note("Use <strong>byte streams</strong> for binary data (images, audio, video). Use <strong>character streams</strong> for text files (they handle Unicode automatically)."))

c8 += sec("📥","Byte Streams","""
"""+code("""<span class="kw">import</span> java.io.*;

<span class="kw">public class</span> <span class="cls">ByteStreamDemo</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) <span class="kw">throws</span> <span class="cls">IOException</span> {
        <span class="cm">// Writing bytes</span>
        <span class="cls">FileOutputStream</span> fos = <span class="kw">new</span> <span class="cls">FileOutputStream</span>(<span class="str">"data.bin"</span>);
        fos.<span class="fn">write</span>(<span class="num">65</span>);  <span class="cm">// writes byte value 65 ('A')</span>
        fos.<span class="fn">write</span>(<span class="kw">new byte</span>[]{<span class="num">72</span>,<span class="num">101</span>,<span class="num">108</span>,<span class="num">108</span>,<span class="num">111</span>}); <span class="cm">// "Hello"</span>
        fos.<span class="fn">close</span>();

        <span class="cm">// Reading bytes</span>
        <span class="cls">FileInputStream</span> fis = <span class="kw">new</span> <span class="cls">FileInputStream</span>(<span class="str">"data.bin"</span>);
        <span class="kw">int</span> b;
        <span class="kw">while</span> ((b = fis.<span class="fn">read</span>()) != -<span class="num">1</span>) {
            <span class="cls">System</span>.out.print((<span class="kw">char</span>) b);
        }
        fis.<span class="fn">close</span>();
    }
}"""))

c8 += sec("📝","Character Streams","""
"""+code("""<span class="kw">import</span> java.io.*;

<span class="kw">public class</span> <span class="cls">CharStreamDemo</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) <span class="kw">throws</span> <span class="cls">IOException</span> {
        <span class="cm">// Writing characters</span>
        <span class="cls">FileWriter</span> fw = <span class="kw">new</span> <span class="cls">FileWriter</span>(<span class="str">"notes.txt"</span>);
        fw.<span class="fn">write</span>(<span class="str">"Java I/O is simple!\n"</span>);
        fw.<span class="fn">write</span>(<span class="str">"Character streams handle Unicode."</span>);
        fw.<span class="fn">close</span>();

        <span class="cm">// Reading characters</span>
        <span class="cls">FileReader</span> fr = <span class="kw">new</span> <span class="cls">FileReader</span>(<span class="str">"notes.txt"</span>);
        <span class="kw">int</span> ch;
        <span class="kw">while</span> ((ch = fr.<span class="fn">read</span>()) != -<span class="num">1</span>) {
            <span class="cls">System</span>.out.print((<span class="kw">char</span>) ch);
        }
        fr.<span class="fn">close</span>();
    }
}"""))

c8 += sec("🚀","BufferedReader & BufferedWriter","""
<p>Buffered streams wrap other streams and add an internal buffer, drastically improving I/O performance by reducing the number of disk operations.</p>
"""+code("""<span class="kw">import</span> java.io.*;

<span class="kw">public class</span> <span class="cls">BufferedDemo</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) <span class="kw">throws</span> <span class="cls">IOException</span> {
        <span class="cm">// Buffered writing</span>
        <span class="cls">BufferedWriter</span> bw = <span class="kw">new</span> <span class="cls">BufferedWriter</span>(<span class="kw">new</span> <span class="cls">FileWriter</span>(<span class="str">"output.txt"</span>));
        bw.<span class="fn">write</span>(<span class="str">"Line 1: Java is powerful"</span>);
        bw.<span class="fn">newLine</span>();
        bw.<span class="fn">write</span>(<span class="str">"Line 2: I/O is efficient"</span>);
        bw.<span class="fn">flush</span>();   <span class="cm">// ensure buffer is written to disk</span>
        bw.<span class="fn">close</span>();

        <span class="cm">// Buffered reading — line by line</span>
        <span class="cls">BufferedReader</span> br = <span class="kw">new</span> <span class="cls">BufferedReader</span>(<span class="kw">new</span> <span class="cls">FileReader</span>(<span class="str">"output.txt"</span>));
        <span class="cls">String</span> line;
        <span class="kw">while</span> ((line = br.<span class="fn">readLine</span>()) != <span class="kw">null</span>) {
            <span class="cls">System</span>.out.println(line);
        }
        br.<span class="fn">close</span>();
    }
}""")+note("<code>readLine()</code> returns <code>null</code> at end of file. Always call <code>close()</code> to release file handles, or use try-with-resources (Java 7+)."))

c8 += sec("📁","File Class","""
<p>The <code>File</code> class represents a file or directory path. It does NOT read or write content — it works with file metadata.</p>
"""+code("""<span class="kw">import</span> java.io.File;

<span class="cls">File</span> f = <span class="kw">new</span> <span class="cls">File</span>(<span class="str">"output.txt"</span>);

<span class="cls">System</span>.out.println(f.<span class="fn">exists</span>());       <span class="cm">// true/false</span>
<span class="cls">System</span>.out.println(f.<span class="fn">getName</span>());      <span class="cm">// output.txt</span>
<span class="cls">System</span>.out.println(f.<span class="fn">length</span>());      <span class="cm">// size in bytes</span>
<span class="cls">System</span>.out.println(f.<span class="fn">isFile</span>());       <span class="cm">// true</span>
<span class="cls">System</span>.out.println(f.<span class="fn">isDirectory</span>()); <span class="cm">// false</span>

<span class="cm">// Create directory</span>
<span class="kw">new</span> <span class="cls">File</span>(<span class="str">"myFolder"</span>).<span class="fn">mkdir</span>();

<span class="cm">// List files in a directory</span>
<span class="cls">File</span> dir = <span class="kw">new</span> <span class="cls">File</span>(<span class="str">"."</span>);
<span class="kw">for</span> (<span class="cls">String</span> name : dir.<span class="fn">list</span>()) <span class="cls">System</span>.out.println(name);"""))

c8 += sec("📖","Append Mode & try-with-resources","""
"""+code("""<span class="cm">// Append to existing file (second argument = true)</span>
<span class="cls">FileWriter</span> fw = <span class="kw">new</span> <span class="cls">FileWriter</span>(<span class="str">"log.txt"</span>, <span class="kw">true</span>);
fw.<span class="fn">write</span>(<span class="str">"New entry appended\\n"</span>);
fw.<span class="fn">close</span>();

<span class="cm">// try-with-resources — auto closes stream (Java 7+)</span>
<span class="kw">try</span> (<span class="cls">BufferedReader</span> br = <span class="kw">new</span> <span class="cls">BufferedReader</span>(<span class="kw">new</span> <span class="cls">FileReader</span>(<span class="str">"log.txt"</span>))) {
    <span class="cls">String</span> line;
    <span class="kw">while</span> ((line = br.<span class="fn">readLine</span>()) != <span class="kw">null</span>)
        <span class="cls">System</span>.out.println(line);
} <span class="cm">// br.close() called automatically</span>""")+note("Always prefer <strong>try-with-resources</strong> over manual <code>close()</code> calls — it is safer and cleaner."))

c8 += body_close("java_w09.html","Week 9: Packages","java_w11.html","Week 11: Exception Handling")
with open(f"{BASE}/java_w10.html","w",encoding="utf-8") as f: f.write(c8)
print("✅ java_w10.html")

# PAGE 9 — Week 11: Exception Handling
toc9 = ["What is an Exception?","Exception Hierarchy","try-catch-finally","throw & throws","Multiple catch Blocks","Nested try","User-defined Exceptions","Common Built-in Exceptions"]
c9 = shell()
c9 += body_open("Week 11 · CO-3","Exception Handling","co3","CO-3",
    "try/catch/finally, throw, throws, Built-in & User-defined Exceptions",
    toc9,"java_w10.html","Week 10: I/O Streams","java_w12.html","Week 12: Multithreading")

c9 += sec("❓","What is an Exception?","""
<p>An <strong>exception</strong> is an abnormal condition that disrupts the normal flow of a program at <strong>runtime</strong>. Java provides a robust mechanism to handle such conditions gracefully.</p>
<table>
<tr><th>Type of Error</th><th>Phase</th><th>Example</th></tr>
<tr><td>Syntax Error</td><td>Compile time</td><td>Missing semicolon, wrong keyword</td></tr>
<tr><td>Logical Error</td><td>Runtime (wrong output)</td><td>Wrong formula used</td></tr>
<tr><td>Runtime Exception</td><td>Runtime (crash)</td><td>Divide by zero, null pointer</td></tr>
</table>
""")

c9 += sec("🌳","Exception Hierarchy","""
<p>All exceptions in Java are subclasses of <code>Throwable</code>:</p>
<pre><code>java.lang.Object
  └── java.lang.Throwable
        ├── java.lang.Error          (JVM errors — do NOT handle)
        │     ├── OutOfMemoryError
        │     ├── StackOverflowError
        │     └── VirtualMachineError
        └── java.lang.Exception      (handle these)
              ├── Checked Exceptions (compile-time)
              │     ├── IOException
              │     ├── SQLException
              │     └── FileNotFoundException
              └── RuntimeException   (unchecked)
                    ├── ArithmeticException
                    ├── NullPointerException
                    ├── ArrayIndexOutOfBoundsException
                    ├── ClassCastException
                    └── NumberFormatException</code></pre>
"""+info("<strong>Checked exceptions</strong> must be handled or declared. <strong>Unchecked exceptions</strong> (RuntimeException subclasses) are optional to handle. <strong>Errors</strong> should never be caught."))

c9 += sec("🛡️","try-catch-finally","""
"""+code("""<span class="kw">public class</span> <span class="cls">ExceptionDemo</span> {
    <span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
        <span class="kw">int</span>[] arr = {<span class="num">10</span>, <span class="num">20</span>, <span class="num">30</span>};

        <span class="kw">try</span> {
            <span class="kw">int</span> result = arr[<span class="num">0</span>] / <span class="num">0</span>; <span class="cm">// ArithmeticException</span>
            arr[<span class="num">5</span>] = <span class="num">99</span>;               <span class="cm">// ArrayIndexOutOfBoundsException</span>
        } <span class="kw">catch</span> (<span class="cls">ArithmeticException</span> e) {
            <span class="cls">System</span>.out.println(<span class="str">"Math error: "</span> + e.getMessage());
        } <span class="kw">catch</span> (<span class="cls">ArrayIndexOutOfBoundsException</span> e) {
            <span class="cls">System</span>.out.println(<span class="str">"Array error: "</span> + e.getMessage());
        } <span class="kw">finally</span> {
            <span class="cls">System</span>.out.println(<span class="str">"Finally always executes!"</span>);
        }
    }
}""")+note("<code>finally</code> always executes — even if a <code>return</code> is in the try block, or an exception is thrown that is not caught. It is used to release resources."))

c9 += sec("🚀","throw & throws","""
<table>
<tr><th>Keyword</th><th>Purpose</th><th>Used in</th></tr>
<tr><td><code>throw</code></td><td>Manually throw an exception object</td><td>Inside a method body</td></tr>
<tr><td><code>throws</code></td><td>Declare that a method may throw an exception</td><td>Method signature</td></tr>
</table>
"""+code("""<span class="cm">// Using 'throw' to manually throw an exception</span>
<span class="kw">static void</span> <span class="fn">validateAge</span>(<span class="kw">int</span> age) {
    <span class="kw">if</span> (age < <span class="num">18</span>)
        <span class="kw">throw new</span> <span class="cls">IllegalArgumentException</span>(<span class="str">"Age must be 18 or above: "</span> + age);
    <span class="cls">System</span>.out.println(<span class="str">"Valid age: "</span> + age);
}

<span class="cm">// Using 'throws' to delegate handling to caller</span>
<span class="kw">static void</span> <span class="fn">readFile</span>(<span class="cls">String</span> path) <span class="kw">throws</span> <span class="cls">IOException</span> {
    <span class="cls">BufferedReader</span> br = <span class="kw">new</span> <span class="cls">BufferedReader</span>(<span class="kw">new</span> <span class="cls">FileReader</span>(path));
    <span class="cls">System</span>.out.println(br.<span class="fn">readLine</span>());
    br.<span class="fn">close</span>();
}

<span class="kw">public static void</span> <span class="fn">main</span>(<span class="cls">String</span>[] args) {
    <span class="kw">try</span> {
        <span class="fn">validateAge</span>(<span class="num">15</span>);
        <span class="fn">readFile</span>(<span class="str">"data.txt"</span>);
    } <span class="kw">catch</span> (<span class="cls">IllegalArgumentException</span> | <span class="cls">IOException</span> e) {
        <span class="cls">System</span>.out.println(<span class="str">"Error: "</span> + e.getMessage());
    }
}"""))

c9 += sec("🎯","Multiple catch Blocks","""
<p>Multiple <code>catch</code> blocks allow handling different exception types separately. Catch order matters — more specific exceptions must come before general ones.</p>
"""+code("""<span class="kw">try</span> {
    <span class="cls">String</span> s = <span class="kw">null</span>;
    s.<span class="fn">length</span>();             <span class="cm">// NullPointerException</span>
    <span class="kw">int</span> x = <span class="cls">Integer</span>.<span class="fn">parseInt</span>(<span class="str">"abc"</span>); <span class="cm">// NumberFormatException</span>
} <span class="kw">catch</span> (<span class="cls">NullPointerException</span> e) {
    <span class="cls">System</span>.out.println(<span class="str">"Null: "</span> + e);
} <span class="kw">catch</span> (<span class="cls">NumberFormatException</span> e) {
    <span class="cls">System</span>.out.println(<span class="str">"Format: "</span> + e);
} <span class="kw">catch</span> (<span class="cls">Exception</span> e) {
    <span class="cm">// catches any other Exception — must be LAST</span>
    <span class="cls">System</span>.out.println(<span class="str">"General: "</span> + e);
}""")+warn("If a parent exception class (like <code>Exception</code>) appears before a child (like <code>NullPointerException</code>), a compile-time error occurs: 'exception already caught'."))

c9 += sec("🪺","Nested try","""
"""+code("""<span class="kw">try</span> {
    <span class="cls">System</span>.out.println(<span class="str">"Outer try"</span>);
    <span class="kw">try</span> {
        <span class="kw">int</span> x = <span class="num">10</span> / <span class="num">0</span>;  <span class="cm">// handled in inner catch</span>
    } <span class="kw">catch</span> (<span class="cls">ArithmeticException</span> e) {
        <span class="cls">System</span>.out.println(<span class="str">"Inner catch: "</span> + e.getMessage());
        <span class="kw">throw new</span> <span class="cls">RuntimeException</span>(<span class="str">"Re-thrown"</span>); <span class="cm">// escalate</span>
    }
} <span class="kw">catch</span> (<span class="cls">RuntimeException</span> e) {
    <span class="cls">System</span>.out.println(<span class="str">"Outer catch: "</span> + e.getMessage());
}"""))

c9 += sec("🛠️","User-defined Exceptions","""
<p>Create custom exceptions by extending <code>Exception</code> (checked) or <code>RuntimeException</code> (unchecked).</p>
"""+code("""<span class="cm">// Custom checked exception</span>
<span class="kw">class</span> <span class="cls">InsufficientFundsException</span> <span class="kw">extends</span> <span class="cls">Exception</span> {
    <span class="kw">private double</span> amount;
    <span class="cls">InsufficientFundsException</span>(<span class="kw">double</span> a) {
        <span class="kw">super</span>(<span class="str">"Insufficient funds. Need: ₹"</span> + a);
        amount = a;
    }
    <span class="kw">double</span> <span class="fn">getAmount</span>() { <span class="kw">return</span> amount; }
}

<span class="kw">class</span> <span class="cls">BankAccount</span> {
    <span class="kw">double</span> balance = <span class="num">1000</span>;

    <span class="kw">void</span> <span class="fn">withdraw</span>(<span class="kw">double</span> amt) <span class="kw">throws</span> <span class="cls">InsufficientFundsException</span> {
        <span class="kw">if</span> (amt > balance)
            <span class="kw">throw new</span> <span class="cls">InsufficientFundsException</span>(amt - balance);
        balance -= amt;
    }
}"""))

c9 += sec("📋","Common Built-in Exceptions","""
<table>
<tr><th>Exception</th><th>Cause</th></tr>
<tr><td>ArithmeticException</td><td>Division by zero</td></tr>
<tr><td>NullPointerException</td><td>Accessing method/field on null reference</td></tr>
<tr><td>ArrayIndexOutOfBoundsException</td><td>Array index &lt; 0 or &gt;= length</td></tr>
<tr><td>NumberFormatException</td><td>Invalid string-to-number conversion</td></tr>
<tr><td>ClassCastException</td><td>Invalid type casting</td></tr>
<tr><td>StackOverflowError</td><td>Infinite recursion</td></tr>
<tr><td>FileNotFoundException</td><td>File path does not exist</td></tr>
<tr><td>IOException</td><td>General I/O failure</td></tr>
<tr><td>StringIndexOutOfBoundsException</td><td>String index out of range</td></tr>
</table>
""")

c9 += body_close("java_w10.html","Week 10: I/O Streams","java_w12.html","Week 12: Multithreading")
with open(f"{BASE}/java_w11.html","w",encoding="utf-8") as f: f.write(c9)
print("✅ java_w11.html")

# PAGE 10 — Week 12: Multithreading
toc10 = ["Process vs Thread","Creating Threads","Thread Lifecycle","Thread Methods","Thread Priorities","Synchronization","Inter-thread Communication"]
c10 = shell()
c10 += body_open("Week 12 · CO-3","Multithreading","co3","CO-3",
    "Thread creation, lifecycle, priorities, synchronization, and inter-thread communication",
    toc10,"java_w11.html","Week 11: Exception Handling","java_w13.html","Week 13: Collection Interfaces")

c10 += sec("⚙️","Process vs Thread","""
<table>
<tr><th>Feature</th><th>Process</th><th>Thread</th></tr>
<tr><td>Definition</td><td>An executing program instance</td><td>Lightweight unit of a process</td></tr>
<tr><td>Memory</td><td>Own memory space</td><td>Shares process memory</td></tr>
<tr><td>Context switch</td><td>Heavy (expensive)</td><td>Light (fast)</td></tr>
<tr><td>Communication</td><td>Complex (IPC)</td><td>Easy (shared memory)</td></tr>
<tr><td>Creation time</td><td>Slow</td><td>Fast</td></tr>
</table>
"""+note("Java supports <strong>multithreading</strong> natively — multiple threads of a single process run concurrently, improving CPU utilization and reducing execution time."))

c10 += sec("🧵","Creating Threads","""
<h3>Method 1: Extending Thread class</h3>
"""+code("""<span class="kw">class</span> <span class="cls">MyThread</span> <span class="kw">extends</span> <span class="cls">Thread</span> {
    <span class="ann">@Override</span>
    <span class="kw">public void</span> <span class="fn">run</span>() {                        <span class="cm">// code that runs in new thread</span>
        <span class="kw">for</span> (<span class="kw">int</span> i = <span class="num">1</span>; i <= <span class="num">5</span>; i++) {
            <span class="cls">System</span>.out.println(<span class="str">"Thread: "</span> + i);
        }
    }
}

<span class="cls">MyThread</span> t = <span class="kw">new</span> <span class="cls">MyThread</span>();
t.<span class="fn">start</span>(); <span class="cm">// start() creates new thread and calls run()</span>""")+"""<h3>Method 2: Implementing Runnable (Preferred)</h3>"""+code("""<span class="kw">class</span> <span class="cls">MyRunnable</span> <span class="kw">implements</span> <span class="cls">Runnable</span> {
    <span class="ann">@Override</span>
    <span class="kw">public void</span> <span class="fn">run</span>() {
        <span class="kw">for</span> (<span class="kw">int</span> i = <span class="num">1</span>; i <= <span class="num">5</span>; i++)
            <span class="cls">System</span>.out.println(<span class="cls">Thread</span>.<span class="fn">currentThread</span>().<span class="fn">getName</span>() + <span class="str">": "</span> + i);
    }
}

<span class="cls">Thread</span> t1 = <span class="kw">new</span> <span class="cls">Thread</span>(<span class="kw">new</span> <span class="cls">MyRunnable</span>(), <span class="str">"Worker-1"</span>);
<span class="cls">Thread</span> t2 = <span class="kw">new</span> <span class="cls">Thread</span>(<span class="kw">new</span> <span class="cls">MyRunnable</span>(), <span class="str">"Worker-2"</span>);
t1.<span class="fn">start</span>();
t2.<span class="fn">start</span>();""")+note("<strong>Runnable is preferred</strong> because Java supports only single inheritance. Implementing Runnable keeps the class free to extend another class."))

c10 += sec("🔄","Thread Lifecycle","""
<table>
<tr><th>State</th><th>Description</th></tr>
<tr><td><strong>New</strong></td><td>Thread object created but <code>start()</code> not yet called</td></tr>
<tr><td><strong>Runnable</strong></td><td>After <code>start()</code> — ready to run, waiting for CPU</td></tr>
<tr><td><strong>Running</strong></td><td>Scheduler picks the thread; <code>run()</code> is executing</td></tr>
<tr><td><strong>Blocked / Waiting</strong></td><td>Waiting for a lock, I/O, or <code>sleep()</code> to expire</td></tr>
<tr><td><strong>Terminated / Dead</strong></td><td><code>run()</code> method has completed</td></tr>
</table>
""")

c10 += sec("🔧","Thread Methods","""
<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>start()</td><td>Creates new thread and invokes run()</td></tr>
<tr><td>run()</td><td>Entry point of thread logic (don't call directly)</td></tr>
<tr><td>sleep(ms)</td><td>Pauses thread for specified milliseconds</td></tr>
<tr><td>join()</td><td>Waits for a thread to complete before continuing</td></tr>
<tr><td>getName()</td><td>Returns thread name</td></tr>
<tr><td>setName(s)</td><td>Sets thread name</td></tr>
<tr><td>getPriority()</td><td>Returns priority (1–10)</td></tr>
<tr><td>setPriority(n)</td><td>Sets thread priority</td></tr>
<tr><td>isAlive()</td><td>Returns true if thread has not terminated</td></tr>
<tr><td>currentThread()</td><td>Returns reference to currently executing thread</td></tr>
</table>
"""+code("""<span class="kw">try</span> {
    t1.<span class="fn">join</span>();  <span class="cm">// main thread waits for t1 to finish</span>
    <span class="cls">Thread</span>.<span class="fn">sleep</span>(<span class="num">500</span>); <span class="cm">// current thread sleeps 500ms</span>
} <span class="kw">catch</span> (<span class="cls">InterruptedException</span> e) {
    e.<span class="fn">printStackTrace</span>();
}"""))

c10 += sec("⭐","Thread Priorities","""
<p>Java thread priorities range from <code>1</code> (MIN_PRIORITY) to <code>10</code> (MAX_PRIORITY), with <code>5</code> as the default (NORM_PRIORITY). Higher priority threads are <em>more likely</em> to be chosen by the scheduler — but this is NOT guaranteed.</p>
"""+code("""<span class="cls">Thread</span> t1 = <span class="kw">new</span> <span class="cls">Thread</span>(task, <span class="str">"High"</span>);
<span class="cls">Thread</span> t2 = <span class="kw">new</span> <span class="cls">Thread</span>(task, <span class="str">"Low"</span>);

t1.<span class="fn">setPriority</span>(<span class="cls">Thread</span>.MAX_PRIORITY); <span class="cm">// 10</span>
t2.<span class="fn">setPriority</span>(<span class="cls">Thread</span>.MIN_PRIORITY); <span class="cm">// 1</span>

t1.<span class="fn">start</span>(); t2.<span class="fn">start</span>();"""))

c10 += sec("🔐","Synchronization","""
<p>When multiple threads access <strong>shared data</strong> simultaneously, data inconsistency (race condition) can occur. <code>synchronized</code> ensures only one thread executes a block/method at a time.</p>
"""+code("""<span class="kw">class</span> <span class="cls">SeatReservation</span> {
    <span class="kw">int</span> availableSeats = <span class="num">100</span>;

    <span class="kw">synchronized void</span> <span class="fn">book</span>(<span class="cls">String</span> passenger) {
        <span class="kw">if</span> (availableSeats > <span class="num">0</span>) {
            availableSeats--;
            <span class="cls">System</span>.out.println(passenger + <span class="str">" booked. Remaining: "</span> + availableSeats);
        } <span class="kw">else</span> {
            <span class="cls">System</span>.out.println(<span class="str">"No seats for "</span> + passenger);
        }
    }
}

<span class="cls">SeatReservation</span> hall = <span class="kw">new</span> <span class="cls">SeatReservation</span>();
<span class="kw">new</span> <span class="cls">Thread</span>(() -> hall.<span class="fn">book</span>(<span class="str">"Ravi"</span>)).start();
<span class="kw">new</span> <span class="cls">Thread</span>(() -> hall.<span class="fn">book</span>(<span class="str">"Priya"</span>)).start();""")+warn("Without synchronization, two threads may both read <code>availableSeats = 1</code>, both decrement it, and the system gives 2 bookings for 1 seat — a classic race condition."))

c10 += sec("💬","Inter-thread Communication","""
<p>Threads communicate via <code>wait()</code>, <code>notify()</code>, and <code>notifyAll()</code> — all defined in <code>Object</code> class and must be called inside <code>synchronized</code> context.</p>
"""+code("""<span class="kw">class</span> <span class="cls">SharedBuffer</span> {
    <span class="kw">int</span> data; <span class="kw">boolean</span> ready = <span class="kw">false</span>;

    <span class="kw">synchronized void</span> <span class="fn">produce</span>(<span class="kw">int</span> val) <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        <span class="kw">while</span> (ready) <span class="kw">wait</span>();   <span class="cm">// wait if not consumed yet</span>
        data = val; ready = <span class="kw">true</span>;
        <span class="cls">System</span>.out.println(<span class="str">"Produced: "</span> + val);
        <span class="fn">notify</span>();               <span class="cm">// wake up consumer</span>
    }

    <span class="kw">synchronized int</span> <span class="fn">consume</span>() <span class="kw">throws</span> <span class="cls">InterruptedException</span> {
        <span class="kw">while</span> (!ready) <span class="kw">wait</span>(); <span class="cm">// wait until data is available</span>
        ready = <span class="kw">false</span>;
        <span class="fn">notify</span>();               <span class="cm">// wake up producer</span>
        <span class="kw">return</span> data;
    }
}"""))

c10 += body_close("java_w11.html","Week 11: Exception Handling","java_w13.html","Week 13: Collection Interfaces")
with open(f"{BASE}/java_w12.html","w",encoding="utf-8") as f: f.write(c10)
print("✅ java_w12.html")

# PAGE 11 — Week 13: Collection Framework Interfaces
toc11 = ["What is the Collection Framework?","Collection Interface","List Interface","Set Interface","Queue Interface","Map Interface","Iterator"]
c11 = shell()
c11 += body_open("Week 13 · CO-4","Collection Framework — Interfaces","co4","CO-4",
    "Collection, List, Set, Queue, and Map interfaces; Iterator",
    toc11,"java_w12.html","Week 12: Multithreading","java_w14.html","Week 14: Collection Classes")

c11 += sec("🗺️","What is the Collection Framework?","""
<p>The <strong>Java Collections Framework</strong> provides a unified architecture for representing and manipulating groups of objects. It includes:</p>
<ul>
<li><strong>Interfaces</strong> — abstract types (Collection, List, Set, Queue, Map)</li>
<li><strong>Classes</strong> — concrete implementations (ArrayList, HashMap, TreeSet...)</li>
<li><strong>Algorithms</strong> — utility methods in <code>Collections</code> class (sort, search, shuffle...)</li>
</ul>
"""+code("""<span class="cm">Hierarchy:</span>
Iterable
  └── Collection
        ├── List      → ArrayList, LinkedList, Vector, Stack
        ├── Set       → HashSet, LinkedHashSet, TreeSet
        └── Queue     → PriorityQueue, ArrayDeque, LinkedList

Map (separate hierarchy)
  ├── HashMap, LinkedHashMap
  └── SortedMap → TreeMap""")+note("By default, collections hold <strong>heterogeneous objects</strong> (any type). Use <strong>Generics</strong> (e.g., <code>List&lt;String&gt;</code>) to restrict to a single type and get type safety."))

c11 += sec("📦","Collection Interface","""
<p>The root interface of the collection hierarchy. All collection types implement it. Key methods:</p>
<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>add(E e)</td><td>Adds element e</td></tr>
<tr><td>remove(Object o)</td><td>Removes specified element</td></tr>
<tr><td>size()</td><td>Returns number of elements</td></tr>
<tr><td>isEmpty()</td><td>Returns true if collection has no elements</td></tr>
<tr><td>contains(Object o)</td><td>Returns true if element is present</td></tr>
<tr><td>iterator()</td><td>Returns an Iterator over elements</td></tr>
<tr><td>clear()</td><td>Removes all elements</td></tr>
<tr><td>toArray()</td><td>Converts collection to array</td></tr>
</table>
""")

c11 += sec("📋","List Interface","""
<p><code>List</code> is an <strong>ordered, index-based</strong> collection that allows <strong>duplicates</strong>.</p>
<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>get(int index)</td><td>Returns element at index</td></tr>
<tr><td>set(int index, E e)</td><td>Replaces element at index</td></tr>
<tr><td>add(int index, E e)</td><td>Inserts at specific position</td></tr>
<tr><td>remove(int index)</td><td>Removes element at index</td></tr>
<tr><td>indexOf(Object o)</td><td>Returns first index of element</td></tr>
<tr><td>subList(from, to)</td><td>Returns a view of portion [from, to)</td></tr>
</table>
"""+code("""<span class="kw">import</span> java.util.*;

<span class="cls">List</span>&lt;<span class="cls">String</span>&gt; names = <span class="kw">new</span> <span class="cls">ArrayList</span>&lt;&gt;();
names.<span class="fn">add</span>(<span class="str">"Alice"</span>);
names.<span class="fn">add</span>(<span class="str">"Bob"</span>);
names.<span class="fn">add</span>(<span class="num">0</span>, <span class="str">"Zara"</span>);       <span class="cm">// insert at front</span>
names.<span class="fn">set</span>(<span class="num">1</span>, <span class="str">"Arjun"</span>);       <span class="cm">// replace index 1</span>
<span class="cls">System</span>.out.println(names);     <span class="cm">// [Zara, Arjun, Bob]</span>
<span class="cls">System</span>.out.println(names.<span class="fn">get</span>(<span class="num">2</span>)); <span class="cm">// Bob</span>"""))

c11 += sec("🔵","Set Interface","""
<p><code>Set</code> is a collection that <strong>does not allow duplicates</strong>. Order depends on implementation.</p>
<table>
<tr><th>Implementation</th><th>Ordering</th><th>Null allowed</th><th>Performance</th></tr>
<tr><td>HashSet</td><td>No guaranteed order</td><td>One null</td><td>O(1) avg</td></tr>
<tr><td>LinkedHashSet</td><td>Insertion order</td><td>One null</td><td>O(1) avg</td></tr>
<tr><td>TreeSet</td><td>Sorted (natural/comparator)</td><td>No null</td><td>O(log n)</td></tr>
</table>
"""+code("""<span class="cls">Set</span>&lt;<span class="cls">String</span>&gt; fruits = <span class="kw">new</span> <span class="cls">HashSet</span>&lt;&gt;();
fruits.<span class="fn">add</span>(<span class="str">"Apple"</span>);
fruits.<span class="fn">add</span>(<span class="str">"Mango"</span>);
fruits.<span class="fn">add</span>(<span class="str">"Apple"</span>); <span class="cm">// duplicate — ignored</span>
<span class="cls">System</span>.out.println(fruits.<span class="fn">size</span>()); <span class="cm">// 2</span>"""))

c11 += sec("🔢","Queue Interface","""
<p><code>Queue</code> follows <strong>FIFO</strong> (First-In-First-Out) ordering. Key methods:</p>
<table>
<tr><th>Method</th><th>Throws exception?</th><th>Returns special value?</th></tr>
<tr><td>add(e) / offer(e)</td><td>add() throws, offer() returns false</td><td>offer() returns false</td></tr>
<tr><td>remove() / poll()</td><td>remove() throws, poll() returns null</td><td>poll() returns null if empty</td></tr>
<tr><td>element() / peek()</td><td>element() throws, peek() returns null</td><td>peek() returns null if empty</td></tr>
</table>
"""+code("""<span class="cls">Queue</span>&lt;<span class="cls">String</span>&gt; queue = <span class="kw">new</span> <span class="cls">LinkedList</span>&lt;&gt;();
queue.<span class="fn">offer</span>(<span class="str">"Task 1"</span>);
queue.<span class="fn">offer</span>(<span class="str">"Task 2"</span>);
queue.<span class="fn">offer</span>(<span class="str">"Task 3"</span>);
<span class="cls">System</span>.out.println(queue.<span class="fn">peek</span>());  <span class="cm">// Task 1 (doesn't remove)</span>
<span class="cls">System</span>.out.println(queue.<span class="fn">poll</span>());  <span class="cm">// Task 1 (removes)</span>
<span class="cls">System</span>.out.println(queue.<span class="fn">size</span>());  <span class="cm">// 2</span>"""))

c11 += sec("🗝️","Map Interface","""
<p><code>Map</code> stores <strong>key-value pairs</strong>. Keys are unique; values can be duplicated. Map does NOT extend Collection.</p>
<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>put(K,V)</td><td>Adds key-value pair; overwrites if key exists</td></tr>
<tr><td>get(K)</td><td>Returns value for key, or null</td></tr>
<tr><td>remove(K)</td><td>Removes entry by key</td></tr>
<tr><td>containsKey(K)</td><td>true if key exists</td></tr>
<tr><td>keySet()</td><td>Returns Set of all keys</td></tr>
<tr><td>values()</td><td>Returns Collection of all values</td></tr>
<tr><td>entrySet()</td><td>Returns Set of Map.Entry pairs</td></tr>
</table>
"""+code("""<span class="cls">Map</span>&lt;<span class="cls">String</span>, <span class="cls">Integer</span>&gt; scores = <span class="kw">new</span> <span class="cls">HashMap</span>&lt;&gt;();
scores.<span class="fn">put</span>(<span class="str">"Alice"</span>, <span class="num">95</span>);
scores.<span class="fn">put</span>(<span class="str">"Bob"</span>, <span class="num">88</span>);
scores.<span class="fn">put</span>(<span class="str">"Alice"</span>, <span class="num">99</span>); <span class="cm">// overwrites Alice's score</span>

<span class="kw">for</span> (<span class="cls">Map.Entry</span>&lt;<span class="cls">String</span>,<span class="cls">Integer</span>&gt; e : scores.<span class="fn">entrySet</span>())
    <span class="cls">System</span>.out.println(e.<span class="fn">getKey</span>() + <span class="str">" → "</span> + e.<span class="fn">getValue</span>());"""))

c11 += sec("🔁","Iterator","""
<p><code>Iterator</code> provides a safe way to traverse collections and remove elements during iteration.</p>
"""+code("""<span class="cls">List</span>&lt;<span class="cls">Integer</span>&gt; nums = <span class="kw">new</span> <span class="cls">ArrayList</span>&lt;&gt;(<span class="cls">Arrays</span>.<span class="fn">asList</span>(<span class="num">1</span>,<span class="num">2</span>,<span class="num">3</span>,<span class="num">4</span>,<span class="num">5</span>));
<span class="cls">Iterator</span>&lt;<span class="cls">Integer</span>&gt; it = nums.<span class="fn">iterator</span>();

<span class="kw">while</span> (it.<span class="fn">hasNext</span>()) {
    <span class="kw">int</span> n = it.<span class="fn">next</span>();
    <span class="kw">if</span> (n % <span class="num">2</span> == <span class="num">0</span>)
        it.<span class="fn">remove</span>(); <span class="cm">// safe removal during iteration</span>
}
<span class="cls">System</span>.out.println(nums); <span class="cm">// [1, 3, 5]</span>""")+warn("Never modify a collection using <code>list.remove()</code> directly while iterating with an iterator — it throws <code>ConcurrentModificationException</code>. Always use <code>it.remove()</code>."))

c11 += body_close("java_w12.html","Week 12: Multithreading","java_w14.html","Week 14: Collection Classes")
with open(f"{BASE}/java_w13.html","w",encoding="utf-8") as f: f.write(c11)
print("✅ java_w13.html")

# PAGE 12 — Week 14: Collection Classes
toc12 = ["ArrayList","LinkedList","HashSet & LinkedHashSet","TreeSet","PriorityQueue","HashMap & LinkedHashMap","TreeMap","Collections Utility Class"]
c12 = shell()
c12 += body_open("Week 14 · CO-4","Collection Classes","co4","CO-4",
    "ArrayList, LinkedList, HashSet, TreeSet, PriorityQueue, HashMap, TreeMap, Collections class",
    toc12,"java_w13.html","Week 13: Collection Interfaces","","")

c12 += sec("📋","ArrayList","""
<p><code>ArrayList</code> is a <strong>resizable array</strong> implementation of <code>List</code>. It provides fast random access (O(1)) but slow insertions/deletions in the middle (O(n)).</p>
"""+code("""<span class="kw">import</span> java.util.*;

<span class="cls">ArrayList</span>&lt;<span class="cls">String</span>&gt; cities = <span class="kw">new</span> <span class="cls">ArrayList</span>&lt;&gt;();
cities.<span class="fn">add</span>(<span class="str">"Hyderabad"</span>);
cities.<span class="fn">add</span>(<span class="str">"Vizag"</span>);
cities.<span class="fn">add</span>(<span class="str">"Chennai"</span>);
cities.<span class="fn">add</span>(<span class="num">1</span>, <span class="str">"Vijayawada"</span>);  <span class="cm">// insert at index 1</span>

<span class="cls">Collections</span>.<span class="fn">sort</span>(cities);          <span class="cm">// alphabetical sort</span>
cities.<span class="fn">remove</span>(<span class="str">"Chennai"</span>);
<span class="cls">System</span>.out.println(cities);         <span class="cm">// [Hyderabad, Vijayawada, Vizag]</span>
<span class="cls">System</span>.out.println(cities.<span class="fn">size</span>()); <span class="cm">// 3</span>""")+note("ArrayList grows automatically when its capacity is exceeded (by 50% each time). Use <code>ArrayList&lt;E&gt;(initialCapacity)</code> when the approximate size is known."))

c12 += sec("🔗","LinkedList","""
<p><code>LinkedList</code> implements both <code>List</code> and <code>Deque</code>. It uses a doubly-linked node structure — fast insertions/deletions (O(1)) but slow random access (O(n)).</p>
"""+code("""<span class="cls">LinkedList</span>&lt;<span class="cls">Integer</span>&gt; ll = <span class="kw">new</span> <span class="cls">LinkedList</span>&lt;&gt;();
ll.<span class="fn">addFirst</span>(<span class="num">10</span>);  ll.<span class="fn">addLast</span>(<span class="num">30</span>);  ll.<span class="fn">add</span>(<span class="num">1</span>, <span class="num">20</span>);
<span class="cls">System</span>.out.println(ll);          <span class="cm">// [10, 20, 30]</span>
<span class="cls">System</span>.out.println(ll.<span class="fn">getFirst</span>()); <span class="cm">// 10</span>
ll.<span class="fn">removeFirst</span>();
<span class="cls">System</span>.out.println(ll);          <span class="cm">// [20, 30]</span>

<span class="cm">// Use as Stack (LIFO)</span>
ll.<span class="fn">push</span>(<span class="num">99</span>); <span class="cls">System</span>.out.println(ll.<span class="fn">pop</span>()); <span class="cm">// 99</span>

<span class="cm">// Use as Queue (FIFO)</span>
ll.<span class="fn">offer</span>(<span class="num">1</span>); ll.<span class="fn">offer</span>(<span class="num">2</span>); <span class="cls">System</span>.out.println(ll.<span class="fn">poll</span>()); <span class="cm">// 1</span>"""))

c12 += sec("🔵","HashSet & LinkedHashSet","""
<table>
<tr><th>Feature</th><th>HashSet</th><th>LinkedHashSet</th></tr>
<tr><td>Order</td><td>No guaranteed order</td><td>Insertion order maintained</td></tr>
<tr><td>Performance</td><td>Fastest</td><td>Slightly slower</td></tr>
<tr><td>Null</td><td>One null allowed</td><td>One null allowed</td></tr>
<tr><td>Duplicate</td><td>Not allowed</td><td>Not allowed</td></tr>
</table>
"""+code("""<span class="cls">Set</span>&lt;<span class="cls">Integer</span>&gt; hs = <span class="kw">new</span> <span class="cls">HashSet</span>&lt;&gt;(<span class="cls">Arrays</span>.<span class="fn">asList</span>(<span class="num">5</span>,<span class="num">3</span>,<span class="num">1</span>,<span class="num">4</span>,<span class="num">2</span>,<span class="num">3</span>));
<span class="cls">System</span>.out.println(hs); <span class="cm">// e.g. [1, 2, 3, 4, 5] — order varies</span>

<span class="cls">Set</span>&lt;<span class="cls">Integer</span>&gt; lhs = <span class="kw">new</span> <span class="cls">LinkedHashSet</span>&lt;&gt;(<span class="cls">Arrays</span>.<span class="fn">asList</span>(<span class="num">5</span>,<span class="num">3</span>,<span class="num">1</span>,<span class="num">4</span>,<span class="num">2</span>,<span class="num">3</span>));
<span class="cls">System</span>.out.println(lhs); <span class="cm">// [5, 3, 1, 4, 2] — insertion order</span>"""))

c12 += sec("🌳","TreeSet","""
<p><code>TreeSet</code> stores elements in <strong>sorted (natural) order</strong> using a Red-Black Tree. For custom objects, implement <code>Comparable</code> or pass a <code>Comparator</code>.</p>
"""+code("""<span class="cls">TreeSet</span>&lt;<span class="cls">String</span>&gt; ts = <span class="kw">new</span> <span class="cls">TreeSet</span>&lt;&gt;();
ts.<span class="fn">add</span>(<span class="str">"Banana"</span>); ts.<span class="fn">add</span>(<span class="str">"Apple"</span>); ts.<span class="fn">add</span>(<span class="str">"Cherry"</span>); ts.<span class="fn">add</span>(<span class="str">"Apple"</span>);
<span class="cls">System</span>.out.println(ts);           <span class="cm">// [Apple, Banana, Cherry] — sorted, no dup</span>
<span class="cls">System</span>.out.println(ts.<span class="fn">first</span>());   <span class="cm">// Apple</span>
<span class="cls">System</span>.out.println(ts.<span class="fn">last</span>());    <span class="cm">// Cherry</span>
<span class="cls">System</span>.out.println(ts.<span class="fn">headSet</span>(<span class="str">"Cherry"</span>)); <span class="cm">// [Apple, Banana]</span>""")+note("For custom sorting: <code>TreeSet&lt;Student&gt; set = new TreeSet&lt;&gt;(Comparator.comparing(s -&gt; s.name));</code>"))

c12 += sec("🏆","PriorityQueue","""
<p><code>PriorityQueue</code> is a <strong>min-heap</strong> by default — the smallest element is always at the head. Use a custom Comparator for max-heap or other ordering.</p>
"""+code("""<span class="cls">PriorityQueue</span>&lt;<span class="cls">Integer</span>&gt; pq = <span class="kw">new</span> <span class="cls">PriorityQueue</span>&lt;&gt;();
pq.<span class="fn">offer</span>(<span class="num">30</span>); pq.<span class="fn">offer</span>(<span class="num">10</span>); pq.<span class="fn">offer</span>(<span class="num">20</span>);

<span class="kw">while</span> (!pq.<span class="fn">isEmpty</span>())
    <span class="cls">System</span>.out.print(pq.<span class="fn">poll</span>() + <span class="str">" "</span>); <span class="cm">// 10 20 30 (min first)</span>

<span class="cm">// Max-heap using Comparator</span>
<span class="cls">PriorityQueue</span>&lt;<span class="cls">Integer</span>&gt; maxPQ = <span class="kw">new</span> <span class="cls">PriorityQueue</span>&lt;&gt;(<span class="cls">Collections</span>.reverseOrder());
maxPQ.<span class="fn">addAll</span>(<span class="cls">Arrays</span>.<span class="fn">asList</span>(<span class="num">30</span>,<span class="num">10</span>,<span class="num">20</span>));
<span class="cls">System</span>.out.print(maxPQ.<span class="fn">poll</span>()); <span class="cm">// 30</span>"""))

c12 += sec("🗝️","HashMap & LinkedHashMap","""
"""+code("""<span class="cls">HashMap</span>&lt;<span class="cls">String</span>,<span class="cls">Integer</span>&gt; map = <span class="kw">new</span> <span class="cls">HashMap</span>&lt;&gt;();
map.<span class="fn">put</span>(<span class="str">"Math"</span>, <span class="num">90</span>); map.<span class="fn">put</span>(<span class="str">"Java"</span>, <span class="num">95</span>); map.<span class="fn">put</span>(<span class="str">"DBMS"</span>, <span class="num">88</span>);
map.<span class="fn">putIfAbsent</span>(<span class="str">"Java"</span>, <span class="num">70</span>);  <span class="cm">// won't overwrite existing</span>

<span class="cm">// Iterate over key-value pairs</span>
map.<span class="fn">forEach</span>((k, v) -> <span class="cls">System</span>.out.println(k + <span class="str">": "</span> + v));

<span class="cm">// Get with default</span>
<span class="kw">int</span> score = map.<span class="fn">getOrDefault</span>(<span class="str">"Physics"</span>, <span class="num">0</span>);

<span class="cm">// LinkedHashMap — maintains insertion order</span>
<span class="cls">Map</span>&lt;<span class="cls">String</span>,<span class="cls">Integer</span>&gt; lhm = <span class="kw">new</span> <span class="cls">LinkedHashMap</span>&lt;&gt;();"""))

c12 += sec("🌲","TreeMap","""
<p><code>TreeMap</code> stores key-value pairs sorted by <strong>key</strong> in natural order.</p>
"""+code("""<span class="cls">TreeMap</span>&lt;<span class="cls">String</span>,<span class="cls">Integer</span>&gt; tm = <span class="kw">new</span> <span class="cls">TreeMap</span>&lt;&gt;();
tm.<span class="fn">put</span>(<span class="str">"Charlie"</span>, <span class="num">3</span>); tm.<span class="fn">put</span>(<span class="str">"Alice"</span>, <span class="num">1</span>); tm.<span class="fn">put</span>(<span class="str">"Bob"</span>, <span class="num">2</span>);
<span class="cls">System</span>.out.println(tm);           <span class="cm">// {Alice=1, Bob=2, Charlie=3} — sorted by key</span>
<span class="cls">System</span>.out.println(tm.<span class="fn">firstKey</span>()); <span class="cm">// Alice</span>
<span class="cls">System</span>.out.println(tm.<span class="fn">lastKey</span>());  <span class="cm">// Charlie</span>"""))

c12 += sec("🔧","Collections Utility Class","""
<p>The <code>java.util.Collections</code> class provides static utility methods for collections.</p>
<table>
<tr><th>Method</th><th>Description</th></tr>
<tr><td>sort(list)</td><td>Sorts list in natural order</td></tr>
<tr><td>sort(list, comparator)</td><td>Sorts with custom comparator</td></tr>
<tr><td>binarySearch(list, key)</td><td>Binary search (list must be sorted)</td></tr>
<tr><td>reverse(list)</td><td>Reverses order of elements</td></tr>
<tr><td>shuffle(list)</td><td>Randomly shuffles elements</td></tr>
<tr><td>min(collection)</td><td>Returns minimum element</td></tr>
<tr><td>max(collection)</td><td>Returns maximum element</td></tr>
<tr><td>frequency(c, obj)</td><td>Counts occurrences of obj</td></tr>
<tr><td>unmodifiableList(list)</td><td>Returns read-only view</td></tr>
<tr><td>synchronizedList(list)</td><td>Returns thread-safe wrapper</td></tr>
</table>
"""+code("""<span class="cls">List</span>&lt;<span class="cls">Integer</span>&gt; nums = <span class="kw">new</span> <span class="cls">ArrayList</span>&lt;&gt;(<span class="cls">Arrays</span>.<span class="fn">asList</span>(<span class="num">5</span>,<span class="num">2</span>,<span class="num">8</span>,<span class="num">1</span>,<span class="num">9</span>));
<span class="cls">Collections</span>.<span class="fn">sort</span>(nums);                             <span class="cm">// [1,2,5,8,9]</span>
<span class="cls">Collections</span>.<span class="fn">reverse</span>(nums);                          <span class="cm">// [9,8,5,2,1]</span>
<span class="cls">System</span>.out.println(<span class="cls">Collections</span>.<span class="fn">max</span>(nums));          <span class="cm">// 9</span>
<span class="cls">System</span>.out.println(<span class="cls">Collections</span>.<span class="fn">frequency</span>(nums, <span class="num">5</span>)); <span class="cm">// 1</span>

<span class="cls">List</span>&lt;<span class="cls">Integer</span>&gt; readOnly = <span class="cls">Collections</span>.<span class="fn">unmodifiableList</span>(nums);
<span class="cm">// readOnly.add(10); // throws UnsupportedOperationException</span>"""))

c12 += body_close("java_w13.html","Week 13: Collection Interfaces","","")
with open(f"{BASE}/java_w14.html","w",encoding="utf-8") as f: f.write(c12)
print("✅ java_w14.html")

print("\n✅ All 12 topic pages generated!")
