import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Your S3 bucket name
bucket_name = 'vishal-lokhande.com'

# List all objects in the S3 bucket
objects = s3.list_objects_v2(Bucket=bucket_name)

# Function to update Content-Type for .html files
def update_content_type():
    if 'Contents' in objects:
        for obj in objects['Contents']:
            key = obj['Key']  # The key (path) of the file in the bucket
            
            # Only target HTML files
            if key.endswith('.html'):
                content_type = 'text/html'
                
                # Print the update being made
                print(f"Updating {key} with Content-Type: {content_type}")
                
                # Copy the object to itself with updated metadata
                copy_source = {'Bucket': bucket_name, 'Key': key}
                
                # Copying the object to itself to update Content-Type
                s3.copy_object(
                    Bucket=bucket_name,
                    Key=key,
                    CopySource=copy_source,
                    MetadataDirective='REPLACE',  # Replace the metadata
                    ContentType=content_type
                )
                print(f"Updated Content-Type for {key} to {content_type}")
            else:
                print(f"Skipped {key}, not an HTML file.")
    else:
        print("No objects found in the bucket.")

# Run the update
update_content_type()
