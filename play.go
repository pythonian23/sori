package main

import (
	vlc "github.com/adrg/libvlc-go/v3"
	"log"
)

var player *vlc.Player

func init() {
	var err error

	if err = vlc.Init("--no-video", "--quiet"); err != nil {
		log.Fatal(err)
	}

	player, err = vlc.NewPlayer()
	if err != nil {
		log.Fatal(err)
	}
}

func Add(source string) error {
	_, err := player.LoadMediaFromURL(source)
	if err != nil {
		return err
	}

	return nil
}
