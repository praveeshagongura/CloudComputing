provider "aws" {
  region = "us-east-1"  # Modify region if needed
}
resource "aws_instance" "my_ec2" {
  ami           = "ami-05b10e08d247fb927"  # Replace with a valid AMI ID
  instance_type = "t2.micro"
  key_name      = "MyKeyPair"  # Replace with an existing AWS key pair
  tags = {
    Name = "TerraformEC2"  # Modify instance name
  }
}
