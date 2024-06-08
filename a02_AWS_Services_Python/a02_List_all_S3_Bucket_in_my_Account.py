import boto3

s3 = boto3.resource('s3')

print(f"\n\t- List of all my Buckets:\n")
for bucket in s3.buckets.all():
    print(f"{bucket.name}")


