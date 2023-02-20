from bs4 import BeautifulSoup

html = """ <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-asib's Blogs</title>
    <link rel="stylesheet" href="asib.css">
</head>

<body >
    <header>
        <h1 id="mobile">welcome to the future</h1>
         <nav id="mobile">
            <a href="about.html">about me</a>
            <a href="ConnectWithUs.html">connect with us</a>
            <a href="document.html">document</a>
            <a href="table.html">table</a>
            <a href="registration.html">register</a>
            <form action="http://www.google.com/search">
            <input type="text" id="search" name="q" placeholder="search somthing">
            <button id="search">search</button>
            </form>
         </nav>
        <hr>
    </header>
    <main>
        <h2>AI</h2>
        <h3>What is AI?</h3>
        <p id="mobile"><abbr title="Artificial intelligence">AI</abbr> refers to the simulation of human intelligence in machines
            that
            are programmed to
            think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits
            associated with a human mind such as learning and problem-solving.</p>
        <p>The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have
            the
            best chance of achieving a specific goal.A subset of artificial intelligence is machine learning, which
            refers
            to the concept that computer programs can automatically learn from and adapt to new data without being
            assisted
            by humans. Deep learning techniques enable this automatic learning through the absorption of huge amounts of
            unstructured data such as text, images, or video</p>
        <h2>AI Branch</h2>
        <!-- nested list -->
        <ul>
            <li>mechine learning
                <ul>
                    <li>roboties</li>
                    <li>smart drone</li>
                </ul>
            </li>
            <li>deep learning
                <ol>
                    <li>data mining</li>
                    <ol type="I">
                        <li>low data</li>
                        <li>high data</li>
                        <li>complex data</li>
                    </ol>
                    <li>big calculation analysis</li>
                </ol>
            </li>
            <li>big data

            </li>
        </ul>
        <section>
            <p class="copy">quate 1: everybody should be drink at least 7 glass of H<sub>2</sub>O <br>
               quate 2: everybody should be know math formula of (a+b)<sup>2</sup>= a<sup>2</sup>+2ab+b<sup>2</sup>
            </p>
        </section>

    </main>

    <hr>
    <footer>
        <!-- <div align="right"> -->
            <section>
        <h2>Contact</h2>
        <address>
            H#138 Dr. Kiyam Uddin Ahmed street <br>
            Mongolbaria, kushtia-7000
        </address>
        <p id="mobile">
            Mobile:+880-1753-249719 <br>
            <a href="https://www.facebook.com/asibahmed11" target="_blank">find on facebook</a>
            <!-- new tab for _blank, same tab or reload _self-->
        </p>
    </section>
        <p class="copy">&copy;copyright by  <span>asib</span></p>
        <!-- </div> -->
    </footer>
</body>

</html> """

soup = BeautifulSoup(html, 'html.parser')

#print(soup.select('#mobile')[0].get_text())
for i in soup.select('#mobile'):
    print(i.get_text())
    print(i.name)
    print(i.attrs)
    print(i.attrs['id'])

other = soup.find('nav')['id']
print(other)