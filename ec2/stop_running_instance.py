
import boto3 


def stop_running_instance():
#Creating an EC2 Client
    ec2 = boto3.client('ec2')

#Gathering all running instances 
    response = ec2.describe_instances(Filters =[{'Name': 'instance-state-name', 'Values': ['running']}, 
    {'Name': 'tag:Environment', 'Values': ['Dev']}])

    running_instances = []

#iterating through the response to extract instance IDs
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            running_instances.append(instance['InstanceId'])
    
#graceful exit if there are no running instances
    if not running_instances:
        print('No running instances')
        return
    
#stopping all running EC2 instances

    ec2.stop_instances(InstanceIds = running_instances)
    
    print(f"These running instances will be stopped: {','.join(running_instances)}")
    



if __name__ == 'main':
    stop_running_instance()






