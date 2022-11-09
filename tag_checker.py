html_tags= {"<html>": "</html>",
            "<body>": "</body>",
            "<head>": "</head>",
            "<title>": "</title>", 
            "<div>": "</div>",
            "<span>": "</span>",
            "<table>": "</table>",
            "<thead>": "</thead>",
            "<tbody>": "</tbody>",
            "<tr>": "</tr>",
            "<td>": "</td>",
            "<script>":  "</script>", 
            "<ul>": "</ul>", 
            "<li>": "</li>",
            "<strong>": "</strong>"}
character_list=[]
tags_list=[]
def tag_checker():
    for character in read:
        character_list.append(character)
    for index in range(len(character_list)):
        character = character_list[index]
        if character == '<':
            position_1 = index 
        elif character == '>':
            position_2 = index + 1
            tag = "".join(character_list[position_1 : position_2])
            split_list = tag.split()
            if len(split_list) > 1 :
                tag_value = split_list[0] + ">"
                tags_list.append(tag_value)
            else :
                tags_list.append(tag)
    one_tag = ['<!doctype>', '<br>', '<img>', '<hr>']
    checking_tags = []
    for a_tag in tags_list:
        if a_tag in one_tag:
            continue
        if a_tag in html_tags:
            checking_tags.append(a_tag)
        elif a_tag in html_tags.values():
            if len(checking_tags)==0:
                print('invalid')
                return True
            elif html_tags[checking_tags[-1]] == a_tag:
                checking_tags.pop()
            else :
                print('invalid')
                return True
    if len(checking_tags) == 0:
        print("valid")
    elif len(checking_tags)!=0:
        print('invalid')
tag_checker()
