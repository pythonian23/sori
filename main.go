package main

import (
	vlc "github.com/adrg/libvlc-go/v3"
	"log"
)

func main() {
	if err := Add("https://stream-uk1.radioparadise.com/mp3-32"); err != nil {
		log.Fatal(err)
	}
	player.Play()

	defer func() {
		player.Stop()
		player.Release()
		vlc.Release()
	}()

	waiter := make(chan struct{})
	<-waiter
}
