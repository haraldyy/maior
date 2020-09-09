def maior():
    maior=0
    for w in range(100):
        c=int(input(''))
        if c>maior:
            maior = c
    return maior
def main():
    print(maior())
if __name__=='__main__':
    main()
