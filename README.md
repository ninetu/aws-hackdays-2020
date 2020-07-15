# AWS Hackdays 2020 Thailand

## Lambda@Edge

1. Create [AWS Lambda Function](https://ap-northeast-1.console.aws.amazon.com/lambda/home?region=ap-northeast-1#/functions)
2. Prepare `t2-ping` script into zip format
```
cd lambdas/t2-ping
zip zip.zip -r .
```

2. Upload zip.zip to AWS Lambda Function

## Greengrass

1. Setup `greengrass` in [AWS Console](https://ap-northeast-1.console.aws.amazon.com/iot/home?region=ap-northeast-1#/greengrassIntro)
- Create a greengrass group
- save certs (*.pem) into ./greengrass/certs/
- save config.json into ./greengrass/config/config.json

2. Run script

```
# create .env from .env-sample then update GROUP_ID, THING_NAME, THING_ARN
cp .env-sample .env

# start docker
docker-compose up -d
```
## Deploy

1. Go to [greengrass group](https://ap-northeast-1.console.aws.amazon.com/iot/home?region=ap-northeast-1#/greengrass/grouphub)
2. Deploy `lambda@edge` to `greengrass group`
