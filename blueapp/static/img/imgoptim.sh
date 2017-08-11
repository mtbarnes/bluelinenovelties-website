#! /bin/bash
for i in $@; do
  mogrify -filter Triangle -define filter:support=2 -thumbnail '1280>' -unsharp 0.25x-.8+8.3+0.045 -dither None -posterize 136 -quality 82 -define jpeg:fancy-upsampling=off -define png:compression-filter=5 -define png:compression-level=9 -define png:compression-strategy=1 -define png:exclude-chunk=all -interlace none -colorspace sRGB $i
  echo "did image "$i
done
