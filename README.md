# Electricity Bill Calculator
This is my private tool to calculate electricity fee for each vendor and export it as a CSV file.

## CSV sample
The exported csv looks like as follows:

| kwh_at | chuden |  htb  |  koyo | sanix | looop | mitsuuroko |
|:------:|:------:|:-----:|:-----:|:-----:|:-----:|:----------:|
|    100 |   2065 |  1956 |  1950 |  6125 |  2400 |       2235 |
|    110 |   2269 |  2150 |  2154 |  6125 |  2640 |       2459 |
|    120 |   2473 |  2343 |  2357 |  6125 |  2880 |       2683 |
|    130 |   2742 |  2598 |  2602 |  6125 |  3120 |       2924 |
|    140 |   3012 |  2854 |  2847 |  6125 |  3360 |       3165 |
|    150 |   3282 |  3110 |  3092 |  6125 |  3600 |       3407 |
|    160 |   3551 |  3365 |  3337 |  6125 |  3840 |       3648 |
|    170 |   3821 |  3621 |  3582 |  6125 |  4080 |       3889 |
|    180 |   4090 |  3876 |  3827 |  6125 |  4320 |       4131 |
|    190 |   4360 |  4132 |  4072 |  6125 |  4560 |       4372 |
|    200 |   4630 |  4388 |  4317 |  6125 |  4800 |       4613 |
|    210 |   4899 |  4643 |  4562 |  6125 |  5040 |       4854 |
|    220 |   5169 |  4899 |  4807 |  6125 |  5280 |       5096 |
|    230 |   5438 |  5155 |  5052 |  6125 |  5520 |       5337 |
|    240 |   5708 |  5410 |  5297 |  6125 |  5760 |       5578 |
|    250 |   5978 |  5666 |  5542 |  6125 |  6000 |       5820 |
|    260 |   6247 |  5921 |  5787 |  6370 |  6240 |       6061 |
|    270 |   6517 |  6177 |  6032 |  6615 |  6480 |       6302 |
|    280 |   6786 |  6433 |  6277 |  6860 |  6720 |       6544 |
|    290 |   7056 |  6688 |  6522 |  7105 |  6960 |       6785 |
|    300 |   7326 |  6944 |  6767 |  7350 |  7200 |       7026 |
|    310 |   7616 |  7219 |  7039 |  7595 |  7440 |       7284 |
|    320 |   7906 |  7495 |  7311 |  7840 |  7680 |       7541 |
|    330 |   8197 |  7770 |  7583 |  8085 |  7920 |       7799 |
|    340 |   8487 |  8045 |  7855 |  8330 |  8160 |       8057 |
|    350 |   8778 |  8321 |  8127 |  8575 |  8400 |       8314 |
|    360 |   9068 |  8596 |  8399 |  8820 |  8640 |       8572 |
|    370 |   9358 |  8872 |  8671 |  9065 |  8880 |       8829 |
|    380 |   9649 |  9147 |  8943 |  9310 |  9120 |       9087 |
|    390 |   9939 |  9422 |  9215 |  9555 |  9360 |       9345 |
|    400 |  10230 |  9698 |  9487 |  9800 |  9600 |       9602 |
|    410 |  10520 |  9973 |  9759 | 10045 |  9840 |       9860 |
|    420 |  10810 | 10249 | 10031 | 10290 | 10080 |      10117 |
|    430 |  11101 | 10524 | 10303 | 10535 | 10320 |      10375 |
|    440 |  11391 | 10799 | 10575 | 10780 | 10560 |      10633 |
|    450 |  11682 | 11075 | 10847 | 11025 | 10800 |      10890 |
|    460 |  11972 | 11350 | 11119 | 11270 | 11040 |      11148 |
|    470 |  12262 | 11626 | 11391 | 11515 | 11280 |      11405 |
|    480 |  12553 | 11901 | 11663 | 11760 | 11520 |      11663 |
|    490 |  12843 | 12176 | 11935 | 12005 | 11760 |      11921 |
|    500 |  13134 | 12452 | 12207 | 12250 | 12000 |      12178 |
|    510 |  13424 | 12727 | 12479 | 12495 | 12240 |      12436 |
|    520 |  13714 | 13003 | 12751 | 12740 | 12480 |      12693 |
|    530 |  14005 | 13278 | 13023 | 12985 | 12720 |      12951 |
|    540 |  14295 | 13553 | 13295 | 13230 | 12960 |      13209 |
|    550 |  14586 | 13829 | 13567 | 13475 | 13200 |      13466 |
|    560 |  14876 | 14104 | 13839 | 13720 | 13440 |      13724 |
|    570 |  15166 | 14380 | 14111 | 13965 | 13680 |      13981 |
|    580 |  15457 | 14655 | 14383 | 14210 | 13920 |      14239 |
|    590 |  15747 | 14930 | 14655 | 14455 | 14160 |      14497 |
|    600 |  16038 | 15206 | 14927 | 14700 | 14400 |      14754 |

## Chart
When you chart it with Google docs it looks something like this.
![エビフライトライアングル](https://docs.google.com/spreadsheets/d/e/2PACX-1vTBTUrfSqSRpKIZkMT3YlhO3yQ1bAq_8DvRTWnyeZLr-KBiaCsBIPc-htUSrUuSEa1tO7dIog135wBb/pubchart?oid=88641024&format=image)

