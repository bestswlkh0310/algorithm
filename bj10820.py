while True:
    try:
        str = list(input())
        print(len([i for i in str if ord('a') <= ord(i) <= ord('z')]), len([i for i in str if ord('A') <= ord(i) <= ord('Z')]), len([i for i in str if ord('0') <= ord(i) <= ord('9')]), str.count(" "))
    except:
        break