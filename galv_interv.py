from collections import Counter

def anagram(w):
    word_list = set(w)
    
    word_dict = {}

    for word in word_list:
            value =  Counter(word)
            key = word 
            word_dict[key] = value
    
    anagrams = []
    for k,v in word_dict.iteritems():
        for k1,v1 in word_dict.iteritems():
            if v == v1 and k != k1 :
                anagrams.extend([k,k1]) 
        
    return list(set(anagrams))

if __name__ == '__main__':
    words = ['bat', 'bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star', 'rats']
    print anagram(words)