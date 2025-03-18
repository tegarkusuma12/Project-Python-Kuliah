def combined_string(string_list):
    output_test_case = []

    for sublist in string_list:
        # Menggabungkan list of strings menjadi satu string, lalu konversi menjadi integer
        combined_number = int(''.join(sublist))
        
        # Tambahkan 1
        combined_number += 1
        
        # Konversi kembali ke string dan pecah menjadi list of strings
        result = list(str(combined_number))

        output_test_case.append(result)
    
    return output_test_case

input_test_case = [['0','01','09'],
                    ['1','5','09'],
                    ['01','00','80']]

output_test_case = combined_string(input_test_case)

print(output_test_case)




        
