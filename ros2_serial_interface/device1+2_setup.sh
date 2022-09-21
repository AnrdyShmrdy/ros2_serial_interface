#!/bin/bash
socat -d -d pty,link=/dev/ttyS0,raw,echo=0 pty,link=/dev/ttyS1,raw,echo=0 &
socat -d -d pty,link=/dev/ttyS2,raw,echo=0 pty,link=/dev/ttyS3,raw,echo=0 &