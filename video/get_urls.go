package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"regexp"
)

type VideoBank struct {
	Videos []struct {
		VideoLink string `json:"video_link"`
	} `json:"videos"`
}

type Content struct {
	VideoBank VideoBank `json:"video_bank"`
}

type ResponseData struct {
	Content Content `json:"content"`
}

func main() {
	resp, err := http.Get("https://www.kia.ru/ajax/page/mediacenter/reviews/more?limit=100&page=1&with_tags=0")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	var responseData ResponseData
	err = json.Unmarshal(body, &responseData)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	videoDict := make(map[string]string)
	regexPattern := regexp.MustCompile(`https:\/\/www\.youtube\.com\/embed\/([\w\W]+)\?.+`)

	for _, el := range responseData.Content.VideoBank.Videos {
		matches := regexPattern.FindStringSubmatch(el.VideoLink)
		if len(matches) > 1 {
			videoID := matches[1]
			videoLink := fmt.Sprintf("https://youtu.be/%s", videoID)
			videoDict[el.VideoLink] = videoLink
		}
	}

	fmt.Println("Video Dictionary:", videoDict)
	fmt.Printf("Количество записей в словаре: %d\n", len(videoDict))

	// Сохранение словаря в файл
	file, err := json.MarshalIndent(videoDict, "", " ")
	if err != nil {
		fmt.Println("Unable to create json", err)
	}
	_ = ioutil.WriteFile("videoDict.json", file, 0644)
}
