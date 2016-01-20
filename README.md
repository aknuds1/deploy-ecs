# Deploy to ECS
This is a collection of scripts for easy deployment to [Amazon ECS](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).

**PLEASE NOTE THAT THIS IS EXPERIMENTAL SOFTWARE**

## Requirements
- Python 3.4
- Docker
- [AWS CLI](https://aws.amazon.com/cli/)

*Make sure that you have logged into your Docker registry and configured the AWS CLI first.*

## Deploy to Staging
The script `deploy-staging` deploys to your staging server.

It implements the following procedure:

1. Deregister old task definitions in the task definition family.
2. Stop old tasks.
3. Tag Docker images corresponding to containers in the task definition with the Git revision.
4. Push the Docker image tags to the corresponding registries.
5. Register new task definition, now referring to Docker images tagged with current Git revisions.
6. Scale down service to 0 instances, in order to be able to update it.
7. Update service to use new task definition and scale service back up to the desired number of
  instances.
