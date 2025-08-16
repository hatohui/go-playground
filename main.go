package main

import (
	"io"
	"log"
	"main/token"
)

func main() {
	randomstring := "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
	tokenizer, err := token.NewTokenizer(randomstring)

	if err != nil {
		log.Fatal(err)
	}

	for {
		token, err := tokenizer.Next()
		if err == io.EOF {
			break
		}

		if err != nil {
			log.Fatal(err)
		}
		
		println("Token:", token)
	}
}