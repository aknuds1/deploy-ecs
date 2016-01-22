# Deploy to ECS
This is a script for easy deployment to [Amazon ECS](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).

## Requirements
- Python 3.4
- Docker
- [AWS CLI](https://aws.amazon.com/cli/)

Before running this script, you must make sure to log into your Docker image registry and configure
the AWS CLI first. Additionally, you must ensure that your AWS ECS agents are able to authenticate
themselves against your Docker image registry in case it is private, by adding the following to
*/etc/ecs/ecs.config* and reboot:

    ECS_ENGINE_AUTH_TYPE=dockercfg
    ECS_ENGINE_AUTH_DATA={"tutum.co":{"auth":"<auth-string>","email":"<my-email>"}}

## Deploy to ECS
The script `deploy-ecs` deploys to your default ECS cluster. You will need task definition and
service JSON files. For this to work, you should have an elastic load balancer and an idle ECS
instance or ensure that the service's deployment configuration specifies a `minimumHealthyPercent`
of less than 100, so that ECS always has an extra node to deploy the new task definition to.
Then ECS will update every node one after the other, so that downtime is avoided.

The script implements the following procedure:

1. Tag Docker images corresponding to containers in the task definition with the Git revision.
2. Push the Docker image tags to the corresponding registries.
3. Deregister old task definitions in the task definition family.
4. Register new task definition, now referring to Docker images tagged with current Git revisions.
5. Update service to use new task definition.
