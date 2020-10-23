import os
import re

translateDict = {
    "Practice this lesson yourself on KhanAcademy.org right now:\n": "现在开始在可汗学院KhanAcademy.org上自行练习本课程：/n",
    "Missed the previous lesson? \n": "错过上节课？\n",
    "About Khan Academy: Khan Academy offers practice exercises, instructional videos, and a personalized learning dashboard that empower learners to study at their own pace in and outside of the classroom. We tackle math, science, computer programming, history, art history, economics, and more. Our math missions guide learners from kindergarten to calculus using state-of-the-art, adaptive technology that identifies strengths and learning gaps. We've also partnered with institutions like NASA, The Museum of Modern Art, The California Academy of Sciences, and MIT to offer specialized content.\n": "关于可汗学院：可汗学院提供练习，教学视频和个性化的学习进度表，使学习者可以在教室内外按自己的步调学习。我们提供数学，科学，计算机编程，历史，艺术史，经济学等等学科的内容。我们的数学任务使用最先进的自适应技术来指导学生从幼儿园到微积分的学习. 这些技术可以识别学习中的优势和差距。我们还与NASA，现代艺术博物馆，加利福尼亚科学院和MIT等机构合作，提供专门的内容。\n",
    "Watch the next lesson: \n": "观看下一节课：\n",
    "For free. For everyone. Forever. #YouCanLearnAnything\n":"免费。为了所有人。永远。 #你可以学习所有东西\n",
    "4th grade math on Khan Academy: 4th grade is the time to start really fine-tuning your arithmetic skills. Not only will you be a multi-digit addition and subtraction rockstar, but you'll extend the multiplication and division that you started in 3rd grade to several digits. You'll also discover that you sometimes have something left over (called a \"remainder\") when you divide. In 3rd grade you learned what a fraction is. Now you'll start adding, subtracting, multiplying, and comparing them. You'll also see how they relate to decimals. On other fronts, you'll learn how to convert between different units (which is super important when comparing the size and speed of robot unicorns in different countries) and continue your journey thinking about various shapes in two dimensions. Some of the foundational concepts of geometry (like lines, rays and angles) also get introduced. As always, we'll round this out with a healthy dose of applied word problems and explorations of number patterns and properties (including the ideas of factors, multiples and prime numbers). The fun must not stop! (Content was selected for this grade level based on a typical curriculum in the United States.)":"可汗学院的四年级数学：四年级是时候开始真正地锻炼您的算术技能了。您不仅会成为多位数的加减法的摇滚明星，而且还将您从三年级开始学的乘法和除法扩展到多位数。有时候做除法您还会发现会剩下一些数（称为“余数”）。在三年级时，您了解了什么是分数。现在，您将开始对它们进行加，减，乘和比较。您还将看到它们与小数之间的关系。在其他方面，您将学习如何在不同的单位之间进行转换（在比较不同国家/地区的机器人独角兽的大小和速度时，这非常重要），并继续着手思考二维的各种形状。此外，还将介绍了一些几何学的基本概念（如线，射线和角度）。与往常一样，我们将通过适量的文字应用题以及对数字模式和性质（包括因子，倍数和质数的概念）的探索来结束。乐趣不能停！ （将根据美国的典型课程选择了该年级水平的内容。）\n",
    "Grade 6th on Khan Academy: By the 6th grade, you're becoming a sophisticated mathemagician. You'll be able to add, subtract, multiply, and divide any non-negative numbers (including decimals and fractions) that any grumpy ogre throws at you. Mind-blowing ideas like exponents (you saw these briefly in the 5th grade), ratios, percents, negative numbers, and variable expressions will start being in your comfort zone. Most importantly, the algebraic side of mathematics is a whole new kind of fun! And if that is not enough, we are going to continue with our understanding of ideas like the coordinate plane (from 5th grade) and area while beginning to derive meaning from data! (Content was selected for this grade level based on a typical curriculum in the United States.)":"可汗学院上的六年级课程：到了六年级，你将成为一名高级数学家。对于暴躁食人魔向你抛出的加，减，乘和非负数（包括小数和小数）除法，你都能轻松应对。一些令人震惊的概念，例如指数（你在五年级时曾看到过），比例，百分比，负数和变量表达式将开始出现在你的舒适区域中。 最重要的是，数学的代数方面是一种全新的乐趣！ 如果这还不够，我们将继续对坐标平面（五年级起）和面积等概念有所了解，同时开始从数据中获取信息！ （该年级水平的内容是根据正常的美国课纲所挑选。）\n",
    "Grade 7th on Khan Academy: 7th grade takes much of what you learned in 6th grade to an entirely new level. In particular, you'll now learn to do everything with negative numbers (we're talking everything--adding, subtracting, multiplying, dividing, fractions, decimals... everything!). You'll also take your algebraic skills to new heights by tackling two-step equations. 7th grade is also when you start thinking about probability (which is super important for realizing that casinos and lotteries are really just ways of taking money away from people who don't know probability) and dig deeper into the world of data and statistics. Onward! (Content was selected for this grade level based on a typical curriculum in the United States.)":"可汗学院（Khan Academy）7年级：7年级将您在6年级中学到的很多知识提高到一个全新的水平。 特别是，您现在将学习使用负数来完成所有操作（我们正在谈论所有内容-加，减，乘，除，分数，小数……所有内容！）。 通过解决两步方程式，您还将把代数技能提高到新的高度。 七年级也是当您开始学习概率（这对于意识到赌场和彩票实际上只是从不知道概率的人身上获取金钱的方式这一点来说非常重要），并更深入地研究数据和统计领域的知识。 向前！（该年级水平的内容是根据正常的美国课纲所挑选。）\n",
    "8th grade on Khan Academy: 8th grade is all about tackling the meat of algebra and getting exposure to some of the foundational concepts in geometry. If you get this stuff (and you should because you're incredibly persistent), the rest of your life will be easy. Okay, maybe not your whole life, but at least your mathematical life. Seriously, if you really get the equations and functions stuff we cover here, most of high school will feel intuitive, even relaxing. (Content was selected for this grade level based on a typical curriculum in the United States.)":"可汗学院（Khan Academy）8年级：八年级是关于解决代数问题，并接触几何学的一些基础概念。 如果您掌握了这些东西（坚持不懈的您也应该这么做），那么您的余生将变得很轻松。 好吧，也许不是您的一生，但至少是您的数学生涯。 认真地说，如果您真正了解了这里讨论的方程式和函数的内容，那么高中期间大部分时候都会感到直觉甚至放松。 （该年级水平的内容是根据正常的美国课纲所挑选。）\n",
    "Pre-Algebra on Khan Academy: No way, this isn't your run of the mill arithmetic. This is Pre-algebra. You're about to play with the professionals. Think of pre-algebra as a runway. You're the airplane and algebra is your sunny vacation destination. Without the runway you're not going anywhere. Seriously, the foundation for all higher mathematics is laid with many of the concepts that we will introduce to you here: negative numbers, absolute value, factors, multiples, decimals, and fractions to name a few. So buckle up and move your seat into the upright position. We're about to take off!":"可汗学院的初级代数：这不是你的九九乘法表，这是初级代数。你将与专业人士一起学习。将初级代数视为一条跑道。你是飞机，而代数是您阳光明媚的度假胜地。没有跑道，你将无处可去。认真地说，所有高级数学的基础都是我们将在此处介绍的许多概念奠定的：负数，绝对值，因子，倍数，小数和分数等。因此，请系好安全带并将座椅移至直立位置。我们即将起飞！\n",
    "About Khan Academy: Khan Academy is a nonprofit with a mission to provide a free, world-class education for anyone, anywhere. We believe learners of all ages should have unlimited access to free educational content they can master at their own pace. We use intelligent software, deep data analytics and intuitive user interfaces to help students and teachers around the world. Our resources cover preschool through early college education, including math, biology, chemistry, physics, economics, finance, history, grammar and more. We offer free personalized SAT test prep in partnership with the test developer, the College Board. Khan Academy has been translated into dozens of languages, and 100 million people use our platform worldwide every year. For more information, visit www.khanacademy.org, join us on Facebook or follow us on Twitter at @khanacademy. And remember, you can learn anything.":"关于可汗学院：可汗学院是一家非营利组织，其使命是为任何地方的任何人提供免费的世界级教育。 我们认为，各个年龄段的学习者都应该可以无限制地访问他们可以按照自己的进度掌握的免费教育内容。 我们使用智能软件，深度数据分析和直观的用户界面来帮助世界各地的学生和教师。 我们的资源涵盖从早期大学教育到学前教育，包括数学，生物学，化学，物理学，经济学，金融，历史，语法等。 我们与测试开发者学院董事会合作提供免费的个性化SAT考试准备。 可汗学院已被翻译成数十种语言，全球每年有1亿人使用我们的平台。 有关更多信息，请访问www.khanacademy.org，在Facebook上加入我们，或在Twitter上@khanacademy关注我们。 记住，您可以学到任何东西。\n",
    "Geometry on Khan Academy: We are surrounded by space. And that space contains lots of things. And these things have shapes. In geometry we are concerned with the nature of these shapes, how we define them, and what they teach us about the world at large--from math to architecture to biology to astronomy (and everything in between). Learning geometry is about more than just taking your medicine (\"It\'s good for you!\"), it\'s at the core of everything that exists--including you. Having said all that, some of the specific topics we\'ll cover include angles, intersecting lines, right triangles, perimeter, area, volume, circles, triangles, quadrilaterals, analytic geometry, and geometric constructions. Wow. That\'s a lot. To summarize: it\'s difficult to imagine any area of math that is more widely used than geometry.\n":"可汗学院的几何： 我们被空间包围。 这个空间包含很多东西。 这些东西都有形状。 在几何学中，我们关注这些形状的性质，如何定义它们以及它们对整个世界带来的启示-从数学到建筑学到生物学再到天文学（以及之间的所有事物）。 学习几何不仅是吃药（“对你有好处！”），它还是包括你在内的所有事物的核心。 综上所述，我们将讨论的一些具体主题包括角度，相交线，直角三角形，周长，面积，体积，圆，三角形，四边形，解析几何和几何构造。 啊，好多啊。 总结一下：很难想象一个比几何运用更广泛的数学领域。\n",
    "Grade 3rd on Khan Academy: We know you've been rocking through 2nd grade adding and subtracting all kinds of whole numbers (up to 2 digits, right?). That's awesome! In 3rd grade math we want you to start using bigger numbers and start multiplying and dividing, too. By the way, did you know that some numbers aren’t actually “whole?” They’re “partially whole.” We call them fractions! We want you to start playing around and having fun with those, too. There's also area, perimeter, and place value to be discovered. Whew. We have so much to do and can't wait to do it with you. Let's go!":"可汗学院的三年级：我们知道，你在二年级里出色地完成了各种整数的加减法（最多两位数）。太棒了！在三年级数学里，你要开始用更大的数字，并且开始进行乘法和除法了。顺便一提，你知道有些数字并不是整数吗？我们称其为分数！我们还希望你能跟分数好好玩。同时还有面积，周长和位值等着你去发现。哇，我们迫不及待地跟你做这些事情了。一起上吧！\n",
    "Algebra I on Khan Academy: Algebra is the language through which we describe patterns. Think of it as a shorthand, of sorts. As opposed to having to do something over and over again, algebra gives you a simple way to express that repetitive process. It's also seen as a \"gatekeeper\" subject. Once you achieve an understanding of algebra, the higher-level math subjects become accessible to you. Without it, it's impossible to move forward. It's used by people with lots of different jobs, like carpentry, engineering, and fashion design. In these tutorials, we'll cover a lot of ground. Some of the topics include linear equations, linear inequalities, linear functions, systems of equations, factoring expressions, quadratic expressions, exponents, functions, and ratios.":"可汗学院的代数I：代数是我们用来描述模式的语言。可以将其视为简写形式。与必须一遍又一遍地重复某件事相反，代数为您提供了一种表达重复过程的简单方法。它是一项重要的基础技能。一旦您了解了代数，就可以学习更高级的数学主题；没有它，就不可能继续前进。从事不同工作的人都要使用代数，例如木工，工程和时装设计。在这些教程中，我们将介绍很多基础知识。其中一些主题包括线性方程，线性不等式，线性函数，方程组，因式分解，二次表达式，指数，函数和比例。\n",
    "High School Math on Khan Academy: Did you realize that the word \"algebra\" comes from Arabic (just like \"algorithm\" and \"al jazeera\" and \"Aladdin\")? And what is so great about algebra anyway? This tutorial doesn't explore algebra so much as it introduces the history and ideas that underpin it.":"可汗学院的高中数学：你知道代数的英文Algebra其实来自于阿拉伯语吗？（就如同算法Algorithm、半岛电视台Al jazeera和阿拉丁Aladdin）。那代数到底为什么那么棒呢？本教程并没有太多探讨代数，而是介绍了其基础知识和历史。\n",
    "Algebra II on Khan Academy: Your studies in algebra 1 have built a solid foundation from which you can explore linear equations, inequalities, and functions. In algebra 2 we build upon that foundation and not only extend our knowledge of algebra 1, but slowly become capable of tackling the BIG questions of the universe. We'll again touch on systems of equations, inequalities, and functions...but we'll also address exponential and logarithmic functions, logarithms, imaginary and complex numbers, conic sections, and matrices. Don't let these big words intimidate you. We're on this journey with you!":"可汗学院的代数II：代数I部分的学习为你打下了坚实的基础，让你可以前往线性方程、不等式和函数的领域进行探索。在代数II这一部分，我们在之前的基础上继续深入，不仅要延伸我们在代数I部分学到的知识，还要慢慢开始研究怎样攻克宇宙的终极难题。我们将再次接触方程组、不等式、函数等方面的知识，还将解决指数及对数函数、对数、虚数及复数、圆锥曲线、矩阵等新问题。不要被这些听上去高深的词汇吓倒。数学之旅上，将始终有我们与你作伴！\n",
    "Linear Algebra on Khan Academy: Have you ever wondered what the difference is between speed and velocity? Ever try to visualize in four dimensions or six or seven? Linear algebra describes things in two dimensions, but many of the concepts can be extended into three, four or more. Linear algebra implies two dimensional reasoning, however, the concepts covered in linear algebra provide the basis for multi-dimensional representations of mathematical reasoning. Matrices, vectors, vector spaces, transformations, eigenvectors/values all help us to visualize and understand multi dimensional concepts. This is an advanced course normally taken by science or engineering majors after taking at least two semesters of calculus (although calculus really isn't a prereq) so don't confuse this with regular high school algebra.":"可汗学院的线性代数：您是否想知道速率和速度之间的区别是什么？ 是否曾尝试在四个维度或六个或七个维度中进行可视化？ 线性代数以二维方式描述事物，但是许多概念可以扩展为三个，四个或更多维度。 线性代数表示二维论证，但是，线性代数涵盖的概念为描述多维空间的数学论证提供了基础。 矩阵，向量，向量空间，变换，特征向量/值都有助于我们可视化和理解多维概念。 这是一门高级课程，通常由科学或工程专业的学生修完至少两个学期的微积分（尽管微积分并不是先修课程）后才上，因此不要将其与普通的高中代数相混淆。\n",
    "Khan Academy is a nonprofit organization with the mission of providing a free, world-class education for anyone, anywhere. We offer quizzes, questions, instructional videos, and articles on a range of academic subjects, including math, biology, chemistry, physics, history, economics, finance, grammar, preschool learning, and more. We provide teachers with tools and data so they can help their students develop the skills, habits, and mindsets for success in school and beyond. Khan Academy has been translated into dozens of languages, and 15 million people around the globe learn on Khan Academy every month. As a 501(c)(3) nonprofit organization, we would love your help! ":"可汗学院是一家非营利组织，其使命是为任何地方的任何人提供免费的世界级教育。 我们提供涵盖数学、生物、化学、物理、历史、经济、金融、语法、学前教育等多个学术领域的测验、习题、讲解视频及文章。我们为教师提供工具和数据等资源，让他们能够帮助学生培养出学业及未来成功所必需的技能、习惯和心态。 可汗学院已被翻译成数十种语言，在世界各地每个月都有1.5亿用户在可汗学院上进行学习。作为一家符合501(c)(3)条款的非营利组织，我们需要你的帮助！\n",
    "Donate or volunteer today! Donate here: https://www.khanacademy.org/donate?utm_source=youtube&utm_medium=desc":"今天就成为我们捐赠人或志愿者吧！在线捐款： https://www.khanacademy.org/donate?utm_source=youtube&utm_medium=desc\n",
    "成为志愿者：https://www.khanacademy.org/contribute?utm_source=youtube&utm_medium=desc":"成为志愿者：https://www.khanacademy.org/contribute?utm_source=youtube&utm_medium=desc\n",
    "About Khan Academy: Khan Academy is a nonprofit with a mission to provide a free, world-class education for anyone, anywhere. We believe learners of all ages should have unlimited access to free educational content they can master at their own pace. We use intelligent software, deep data analytics and intuitive user interfaces to help students and teachers around the world. Our resources cover preschool through early college education, including math, biology, chemistry, physics, economics, finance, history, grammar and more. We offer free personalized SAT test prep in partnership with the test developer, the College Board. Khan Academy has been translated into dozens of languages, and 100 million people use our platform worldwide every year. For more information, visit www.khanacademy.org, join us on Facebook or follow us on Twitter at @khanacademy. And remember, you can learn anything.":"关于可汗学院：可汗学院是一家非营利组织，其使命是为任何地方的任何人提供免费的世界一流的教育。 我们认为，所有年龄段的学习者都应无限制地访问他们可以按照自己的进度掌握的免费教育内容。 我们使用智能软件，深度数据分析和直观的用户界面来帮助世界各地的学生和教师。 我们的资源涵盖从早期大学教育到学前教育，包括数学、生物、化学、物理、经济学、金融、历史、语法等。 我们与测试开发者大学委员会合作，提供免费的个性化SAT考试准备。 可汗学院已被翻译成数十种语言，全球每年有1亿人使用我们的平台。 有关更多信息，请访问www.khanacademy.org，在Facebook上加入我们，或在Twitter上@khanacademy关注我们。 请记住，您可以学到任何东西。\n",
    "Precalculus on Khan Academy: You may think that precalculus is simply the course you take before calculus. You would be right, of course, but that definition doesn't mean anything unless you have some knowledge of what calculus is. Let's keep it simple, shall we? Calculus is a conceptual framework which provides systematic techniques for solving problems. These problems are appropriately applicable to analytic geometry and algebra. Therefore....precalculus gives you the background for the mathematical concepts, problems, issues and techniques that appear in calculus, including trigonometry, functions, complex numbers, vectors, matrices, and others. There you have it ladies and gentlemen....an introduction to precalculus!":"可汗学院的微积分预科：您可能认为微积分预科只是微积分之前的课程。 这当然不算错，但是除非您对微积分是什么有所了解，否则该定义并没有任何意义。 让我们简单一些吧？ 微积分是一个提供解决问题的系统方法的概念框架。 这些问题适用于解析几何和代数。 因此，微积分预科为您提供微积分中出现的数学概念，问题，课题和方法的背景知识，包括三角函数，函数，复数，向量，矩阵等。 女士们，先生们，这就是微积分预科的介绍！\n",
    "Trigonometry on Khan Academy: Big, fancy word, right? Don't be fooled. Looking at the prefix, tri-, you could probably assume that trigonometry (\"trig\" as it's sometimes called) has something to do with triangles. You would be right! Trig is the study of the properties of triangles. Why is it important? It's used in measuring precise distances, particularly in industries like satellite systems and sciences like astronomy. It's not only space, however. Trig is present in architecture and music, too. Now you may wonder...how is knowing the measurement and properties of triangles relevant to music?? THAT is a great question. Maybe you'll learn the answer from us in these tutorials!":"可汗学院的三角学：听着很高大上是不是？ 但不要上当。 看名字你就知道三角学与三角形有关。 没错，三角学是对三角形性质的研究。 它为什么如此重要？ 它被用于测量精确距离，尤其是在卫星系统和天文学等科学领域。 但是，不仅是在太空里。 三角学也出现在建筑和音乐中。 那你现在可能想知道...学习测量三角形的数据和性质跟音乐有什么关系呢？这是一个很大的问题。 也许你会在这些教程中从我们这得到答案！\n",
    "AP Calculus AB on Khan Academy: Bill Scott uses Khan Academy to teach AP Calculus at Phillips Academy in Andover, Massachusetts, and heÕs part of the teaching team that helped develop Khan AcademyÕs AP lessons. Phillips Academy was one of the first schools to teach AP nearly 60 years ago.":"可汗学院上的AP微积分AB：在马塞诸塞州安多福（Andover）的菲利普斯学院（Phillips Academy）里，Bill Scott 用可汗学院来教AP微积分，同时他也是开发可汗学院AP课程的教学团队的一员。菲利普斯学院是60年前第一批提供AP课程的学校之一。\n",
    "Finance and capital markets on Khan Academy: This is an older tutorial (notice the low-res, bad handwriting) about one of the coolest numbers in reality and how it falls out of our innate desire to compound interest continuously.":"可汗学院上的金融和资本市场：这是一个关于现实中最神奇的数字以及它是如何摆脱我们想连续收取复利的幻想的教程。（可从这些低分辨率的烂手写中看出这是个比较老的教程）\n",
    "Subscribe to Khan Academy: https://www.youtube.com/subscription_center?add_user=khanacademy\n": "订阅可汗学院KhanAcademy: https://www.youtube.com/subscription_center?add_user=khanacademy\n",
    "Subscribe to Khan Academy's \\w* channel:\n": "订阅可汗学院Khan Academy的 <subject name> 频道：\n",
    "Subscribe to Khan Academy: \n": "订阅可汗学院KhanAcademy: \n"
}

def translateDesc(inputFileName, outputFileName):
    # Opens the file that we're trying to translate
    textFile = open(inputFileName, "r")
    fileLines = textFile.readlines()
    textFile.close()

    # Creates an output list and translate line by line
    outputList = []
    for line in fileLines:
        outputList.append(translateLines(line)) #outputList now contains some string in Chinese

    # Creates an output file and writes in it
    outputFile = open(outputFileName, "wb")
    for lines in outputList:
        outputFile.write(lines.encode("utf8"))
    outputFile.close()

def translateLines(line):
    if line in translateDict:
        return translateDict[line]
    else:
        return find_match(translateDict, line)

def find_match(d, line):
    keys = list(d.keys())
    for i in range(len(keys)):
        if (re.match(keys[i], line) is not None):
            return d[keys[i]] 
    return line

#C:\Users\abool\Anaconda3\Scripts\ipython.exe
#cd C:\Users\abool\Desktop\Khan Academy Translate