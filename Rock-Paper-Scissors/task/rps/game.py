# Write your code here
import random
def get_current_score(user_name):
    score = '0'
    is_exist_username = False
    read_file = open('rating.txt', 'r')
    for record in read_file:
        if user_name in record:
            score = record.split(" ")[1].strip('\n')
            is_exist_username = True
            break
    if is_exist_username == False:
        write_file = open('rating.txt', 'a')
        write_file.write(f'{user_name} 0\n')
        write_file.close()
    read_file.close()
    return int(score)

# rules = {'rock':'scissors',
#         'paper':'rock',
#        'scissors':'paper'}
all_options = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
win_mark = 7

user_name = input('Enter your name: ')
print(f'Hello, {user_name}')
current_score = get_current_score(user_name)

select_options = input()
if select_options == '':
    select_options = ['rock', 'scissors', 'paper']
else:
    select_options = select_options.split(',')
print("\nOkay, let's start")

while True:
    user_option = input()
    if user_option == "!exit":
        print("Bye!")
        break
    elif user_option == '!rating':
        print(f'Your rating: {current_score}')
    elif user_option not in select_options:
        print("Invalid input")
    else:
        computer_option = random.choice(select_options)
        current_index = all_options.index(user_option)
        beated_options = []
        if current_index >= len(all_options) - win_mark:
            if current_index == len(all_options) - 1:
                beated_options = all_options[0 : current_index + win_mark - len(all_options) + 1]
            else:
                option1 = ' '.join(all_options[current_index + 1 : ])
                option2 = ' '.join(all_options[0 : current_index + win_mark - len(all_options) + 1])
                beated_options = (option1 + ' ' + option2).split(' ')
        else:
            beated_options = all_options[current_index + 1 : current_index + 1 + win_mark]

        if user_option == computer_option:
            #read_file = open('rating.txt', 'r')
            #all_record = []
            #for line in read_file:
                #if user_name in line:
                    #all_record.append(f'{user_name} {50 + get_current_score(user_name)}\n')
                #else:
                    #all_record.append(line)
            #read_file.close()
            #write_file = open('rating.txt', 'w')
            #write_file.writelines(all_record)
            #write_file.close()
            current_score += 50
            print(f"There is a draw ({computer_option})")
        elif computer_option in beated_options:

            #read_file = open('rating.txt', 'r')
            #all_record = []
            #for line in read_file:
                #if user_name in line:
                    #all_record.append(f'{user_name} {100 + get_current_score(user_name)}\n')
                #else:
                    #all_record.append(line)
            #read_file.close()
            #write_file = open('rating.txt', 'w')
            #write_file.writelines(all_record)
            #write_file.close()
            current_score += 100
            print(f"Well done. Computer chose {computer_option} and failed")
        else:
            print(f"Sorry, but computer chose {computer_option}")


