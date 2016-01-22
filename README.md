# Deploy to ECS
This is a collection of scripts for easy deployment to [Amazon ECS](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).

**PLEASE NOTE THAT THIS IS EXPERIMENTAL SOFTWARE**

## Requirements
- Python 3.4
- Docker
- [AWS CLI](https://aws.amazon.com/cli/)

*Make sure that you have logged into your Docker registry and configured the AWS CLI first.*

## Deploy to Staging
The script `deploy-staging` deploys to your staging server. You will need task definition and
service JSON files.

It implements the following procedure:

1. Tag Docker images corresponding to containers in the task definition with the Git revision.
2. Push the Docker image tags to the corresponding registries.
3. Deregister old task definitions in the task definition family.
4. Register new task definition, now referring to Docker images tagged with current Git revisions.
5. Update service to use new task definition.
