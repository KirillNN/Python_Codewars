def capitalize(s):
    res_1 = res_2 = ''
    for i, v in enumerate(s):
        if i % 2:
            res_1 += v.upper()
            res_2 += v
        else:
            res_2 += v.upper()
            res_1 += v
    return [res_2, res_1]


print(capitalize("abcdef"))

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(capitalize("abcdef"), ['AbCdEf', 'aBcDeF'])
#         test.assert_equals(capitalize("codewars"), ['CoDeWaRs', 'cOdEwArS'])
#         test.assert_equals(capitalize("abracadabra"), ['AbRaCaDaBrA', 'aBrAcAdAbRa'])
#         test.assert_equals(capitalize("codewarriors"), ['CoDeWaRrIoRs', 'cOdEwArRiOrS'])
#         test.assert_equals(capitalize("indexinglessons"), ['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs'])
#         test.assert_equals(capitalize("codingisafunactivity"), ['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY'])
