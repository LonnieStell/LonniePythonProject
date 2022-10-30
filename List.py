aws_list = []

aws_list.append('EC2')
aws_list.append('VPC')
aws_list.append('S3')
aws_list.append('Elastic Beanstalk')
aws_list += [5,6,7]

print(aws_list)
print('There are', len(aws_list), 'item(s) in this list')

del aws_list[5]
del aws_list[5]
del aws_list[4]

print(aws_list)
print('There are', len(aws_list), 'item(s) in this list')