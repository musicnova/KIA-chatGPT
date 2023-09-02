fetch("https://www.kia.ru/ajax/page/mediacenter/reviews/more?limit=100&page=1&with_tags=0")
    .then((r) => r.json())
    .then((r) => {
        let videoDict = {};

        r.content.video_bank.videos.forEach((el, index) => {
            const original_link = el.video_link;
            const video_link = `https://youtu.be/${el.video_link.match(/https:\/\/www\.youtube\.com\/embed\/([\w\W]+)\?.+/)[1]}`;

            videoDict[original_link] = video_link;
        });

        console.log(videoDict);
        console.log(`Количество записей в словаре: ${Object.keys(videoDict).length}`);
});
