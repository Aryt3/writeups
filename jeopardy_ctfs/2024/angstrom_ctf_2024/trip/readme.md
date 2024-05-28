# trip

## Description
```
What road was this this photo taken on?

For example, if the road was "Colesville Road" the flag would be actf{colesville}.
```

## Provided Files
<div style="text-align:center;">
    <img src="https://github.com/Aryt3/writeups/tree/main/jeopardy_ctfs/2024/angstrom_ctf_2024/trip/trip.jpeg" alt="Image" />
</div>

## Writeup

Starting off, we got a picture of some kind and a description which tasks us with some kind of `OSINT`. <br/>
Before doing some kind of `reverse image search` though it's important to check for useful metadata of the image. <br/>
```sh
$ exiftool trip/trip.jpeg 
ExifTool Version Number         : 12.76
File Name                       : trip.jpeg
Directory                       : trip
File Size                       : 1906 kB
File Modification Date/Time     : 2024:05:26 15:13:07+02:00
File Access Date/Time           : 2024:05:26 15:13:07+02:00
File Inode Change Date/Time     : 2024:05:26 15:13:07+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : Apple
Camera Model Name               : iPhone 15 Pro
Orientation                     : Horizontal (normal)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : 17.4.1
Modify Date                     : 2024:04:18 05:54:34
Host Computer                   : iPhone 15 Pro
Exposure Time                   : 1/33
F Number                        : 1.8
Exposure Program                : Program AE
ISO                             : 1000
Exif Version                    : 0232
Date/Time Original              : 2024:04:18 05:54:34
Create Date                     : 2024:04:18 05:54:34
Offset Time                     : -04:00
Offset Time Original            : -04:00
Offset Time Digitized           : -04:00
Shutter Speed Value             : 1/33
Aperture Value                  : 1.8
Brightness Value                : -1.96305564
Exposure Compensation           : 0
Metering Mode                   : Multi-segment
Flash                           : Off, Did not fire
Focal Length                    : 6.8 mm
Subject Area                    : 2849 2137 3291 1884
Maker Note Version              : 14
Run Time Flags                  : Valid
Run Time Value                  : 93549684320583
Run Time Scale                  : 1000000000
Run Time Epoch                  : 0
AE Stable                       : Yes
AE Target                       : 94
AE Average                      : 98
AF Stable                       : Yes
Acceleration Vector             : -0.998894095 -0.03494079414 0.1559448392
Focus Distance Range            : 0.79 - 1.05 m
Content Identifier              : 16FBDA70-FEFF-461C-ABC7-BA696196F8B6
Image Capture Type              : Unknown (12)
Live Photo Video Index          : 8594137124
HDR Headroom                    : 1.00999999
Signal To Noise Ratio           : 27.56163594
Photo Identifier                : EBB944CB-9EED-45A4-B1FB-098E21631CC5
Focus Position                  : 50
HDR Gain                        : 1.893541217
AF Measured Depth               : 1084
AF Confidence                   : 0
Semantic Style                  : {_0=1,_1=0,_2=0,_3=0}
Front Facing Camera             : No
Sub Sec Time Original           : 337
Sub Sec Time Digitized          : 337
Color Space                     : Uncalibrated
Exif Image Width                : 5712
Exif Image Height               : 4284
Sensing Method                  : One-chip color area
Scene Type                      : Directly photographed
Exposure Mode                   : Auto
White Balance                   : Auto
Focal Length In 35mm Format     : 24 mm
Lens Info                       : 2.220000029-9mm f/1.779999971-2.8
Lens Make                       : Apple
Lens Model                      : iPhone 15 Pro back triple camera 6.765mm f/1.78
Composite Image                 : General Composite Image
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Altitude Ref                : Above Sea Level
GPS Time Stamp                  : 09:54:33.79
GPS Speed Ref                   : km/h
GPS Speed                       : 24.30299757
GPS Img Direction Ref           : True North
GPS Img Direction               : 101.5118084
GPS Dest Bearing Ref            : True North
GPS Dest Bearing                : 101.5118084
GPS Date Stamp                  : 2024:04:18
GPS Horizontal Positioning Error: 4.788654674 m
Profile CMM Type                : Apple Computer Inc.
Profile Version                 : 4.0.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2022:01:01 00:00:00
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Apple Computer Inc.
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Apple Computer Inc.
Profile ID                      : ecfda38e388547c36db4bd4f7ada182f
Profile Description             : Display P3
Profile Copyright               : Copyright Apple Inc., 2022
Media White Point               : 0.96419 1 0.82489
Red Matrix Column               : 0.51512 0.2412 -0.00105
Green Matrix Column             : 0.29198 0.69225 0.04189
Blue Matrix Column              : 0.1571 0.06657 0.78407
Red Tone Reproduction Curve     : (Binary data 32 bytes, use -b option to extract)
Chromatic Adaptation            : 1.04788 0.02292 -0.0502 0.02959 0.99048 -0.01706 -0.00923 0.01508 0.75168
Blue Tone Reproduction Curve    : (Binary data 32 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 32 bytes, use -b option to extract)
Image Width                     : 5712
Image Height                    : 4284
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Run Time Since Power Up         : 1 days 1:59:10
Aperture                        : 1.8
Image Size                      : 5712x4284
Megapixels                      : 24.5
Scale Factor To 35 mm Equivalent: 3.5
Shutter Speed                   : 1/33
Create Date                     : 2024:04:18 05:54:34.337-04:00
Date/Time Original              : 2024:04:18 05:54:34.337-04:00
Modify Date                     : 2024:04:18 05:54:34-04:00
GPS Altitude                    : 1 m Above Sea Level
GPS Date/Time                   : 2024:04:18 09:54:33.79Z
GPS Latitude                    : 37 deg 56' 23.60" N
GPS Longitude                   : 75 deg 26' 17.11" W
Circle Of Confusion             : 0.008 mm
Field Of View                   : 73.7 deg
Focal Length                    : 6.8 mm (35 mm equivalent: 24.0 mm)
GPS Position                    : 37 deg 56' 23.60" N, 75 deg 26' 17.11" W
Hyperfocal Distance             : 3.04 m
Light Value                     : 3.4
Lens ID                         : iPhone 15 Pro back triple camera 6.765mm f/1.78
``` 

Seeing that the image contains the coordinates where it was taken in the `meta-data` we can make a simple `goolge-maps` search to retrieve the street-name. <br/>
A quick [google-maps-search](`https://www.google.com/maps/place/37%C2%B056'23.6%22N+75%C2%B026'17.1%22W/@37.9398889,-75.440661,17z/data=!3m1!4b1!4m4!3m3!8m2!3d37.9398889!4d-75.4380861?entry=ttu`) reveals the flag `actf{chinoteague}` which concludes this writeup.