# SVED

*Simple Video Encoding - Distributed*

Web UI to distribute video encoding to an arbitrary number of workers.  Pronounced "Ess-Ved", rhymes with the phrase "Chess Dead".

## Rationale

### Problem Statement

I have a lot of DVDs and Blu-rays that I've digitized for easier use, but they take up far too much space.  Instead of buying more hard drives, which was an option in ye olden times, I decided to learn how to encode video on my own.  This also makes the files compatible with my TV, phone, and PS4, so I don't have to transcode them when watching.

### Solution

Given a set of input file(s), SVED will create encode tasks that worker nodes can run.  The worker nodes will download the source file from SVED, encode it using predefined values (specifics described elsewhere), then upload it back to SVED.  While encoding, the workers send information to SVED which the user can see.

SVED uses RabbitMQ to distribute tasks to workers, a basic First-In-First-Out queue.

### Previously attempted solutions

1. Encode everything on my computer.  Pro: I have full control and can see what's going on.  Cons: Slow for my library.  I can't use my computer while a video is being encoded.  I like using my computer.  Not sustainable.
2. Encode on one of the servers in my homelab by running Handbrake via [jlesage's Handbrake Docker container](https://github.com/jlesage/docker-handbrake).  Pros: I have full control and can see what's going on.  I can use my computer.  Cons: Slow for my library.  Better option must exist.
3. 2, but running on many of my servers at once.  Pros: Full control, I can see what's going on, faster.  Cons: I have to manually decide which server encodes which file, I have to check a new tab for the status of each, sometimes the slowest server will encode the hardest-to-encode file.  Better option must exist.
4. Pre-calculate the encoding power of each server (i.e. the average encoding rate), then write a script to optimally distribute encode tasks to each server.  Pros: Full control, can see what's going on, faster, encodes are completed most optimally.  Cons: Pre-calculating encoding power requires benchmarking (manual work, barf) and can change depending on the file and encoding settings.  Works.  Better solution must exist.
5. 4, but move over to using FFmpeg.  Pros: the above, plus it deals with Handbrake not using the full color range but only limited (so chopping off the top and bottom 16 colors, IIRC).  Cons: learning ffmpeg (just kidding, I learned it's actually surprisingly simple and easy), no longer do I have a nice GUI to see what's going on.

# Note on AI Usage

Literally none.  I made this because I wanted to, not because I wanted a machine to do it for me.

Which is frustrating because, when changing my username and email, I overwrote all my changes over the last 4 years, so now it looks like one commit from 2022 and a dozen all at the same time in 2026.  I guess take me at my word that there's no LLM output in here, just my own pure incompetence. 
