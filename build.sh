#!/bin/bash

docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7,linux/arm/v6 -t bjun626/notion_sync --push .