//control hat position
if image_index == 0 or image_index == 4
    {
    hatOffset = 0;
    }
if image_index == 1 or image_index == 3
    {
    hatOffset = -1;
    }
if image_index == 2
    {
    hatOffset = -3;
    }
if image_index == 5 or image_index == 7
    {
    hatOffset = 1;
    }
if image_index == 6
    {
    hatOffset = 3;
    }

    

hatX = x+(6*faceDir)+(faceDir*hatOffset)
hatY = y-32

