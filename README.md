### BeautifulSoup_LangChain_chatGPT
Web parsing for AI Dialog System based on chatGPT


<!DOCTYPE html>
<html>
<head>
    <title>Отображение README.md</title>
</head>
<body>
    <div id="content"></div>

    <script>
        // Загрузка README.md файла
        fetch('https://raw.githubusercontent.com/terrainternship/KIA-GPT/main/Dmitrii_Panfilov/README.md')
        .then(response => response.text())
        .then(data => {
            const contentDiv = document.getElementById('content');
            const lines = data.split('\n');

            // Парсинг строки для простого Markdown -> HTML преобразования
            lines.forEach(line => {
                let htmlLine = "";

                if (line.startsWith("## ")) {
                    htmlLine = `<h2>${line.substr(3)}</h2>`;
                } else if (line.startsWith("# ")) {
                    htmlLine = `<h1>${line.substr(2)}</h1>`;
                } else if (line.startsWith("- ")) {
                    htmlLine = `<li>${line.substr(2)}</li>`;
                } else {
                    htmlLine = `<p>${line}</p>`;
                }

                contentDiv.innerHTML += htmlLine;
            });
        })
        .catch((error) => console.error('Ошибка загрузки README.md:', error));
    </script>
</body>
</html>
