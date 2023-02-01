# Image-Search-Engine
This engine finds similar images from a bunch of images and output the images most similar to the queried image. 

I used calcHist function in OpenCV to extract the colour histogram of images. Then I utilized two OpenCV similarity functions using Correlation Test and Bhattacharya Distance to compare the histograms of dataset with queried image. Based on the similarity features inquired from histograms, the similar images are short-listed. 

![image](https://user-images.githubusercontent.com/83055325/216028769-1706af66-a32c-4bcc-bcba-521f92d5f0fd.png)

Query Image

![sp6](https://user-images.githubusercontent.com/83055325/216029055-f7a14e32-3ba4-4876-8a94-21a27d03b821.jpg)

Results

![Figure 2023-02-01 164935 (0)](https://user-images.githubusercontent.com/83055325/216028842-fca6ee2a-3ebe-4493-8b3a-ce81d139eaf4.png)
![Figure 2023-02-01 164935 (3)](https://user-images.githubusercontent.com/83055325/216029403-74f6ddca-9633-4f1d-b24c-72cdb8d56053.png)
![Figure 2023-02-01 164935 (7)](https://user-images.githubusercontent.com/83055325/216029274-5a8c5d88-865a-427d-88a1-134ce49c43d0.png)
![Figure 2023-02-01 164935 (8)](https://user-images.githubusercontent.com/83055325/216029251-fb45dd6a-64b2-4794-b910-282729ed7447.png)
![Figure 2023-02-01 164935 (10)](https://user-images.githubusercontent.com/83055325/216028886-29bbdd08-b10b-4a93-9d9d-9c21e834688d.png)
![Figure 2023-02-01 164935 (11)](https://user-images.githubusercontent.com/83055325/216028898-f8cf691d-d978-4463-8d30-2d451aa58583.png)

Histograms

![Figure 2023-02-01 164935 (1)](https://user-images.githubusercontent.com/83055325/216029538-dea9eb31-5c16-429a-817a-414b69cf4807.png)
![Figure 2023-02-01 164935 (5)](https://user-images.githubusercontent.com/83055325/216029543-da41dde0-6e37-49f9-9c17-8fcd2715dfab.png)
![Figure 2023-02-01 164935 (9)](https://user-images.githubusercontent.com/83055325/216029548-248dbc43-c091-46b3-bfd6-63545c124d4f.png)
