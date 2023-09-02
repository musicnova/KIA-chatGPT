fetch("https://www.kia.ru/ajax/page/mediacenter/reviews/more?limit=100&page=1&with_tags=0").then((r) => r.json()).then((r) => {
        let temp = "";
        r.content.video_bank.videos.forEach((el, index) => {
        const video_link = `https://youtu.be/${el.video_link.match(/https:\/\/www\.youtube\.com\/embed\/([\w\W]+)\?.+/)[1]}`
        temp += `${video_link}\n`
         })
    console.log(temp)
})
