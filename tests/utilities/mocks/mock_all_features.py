MOCK_ALL_FEATURES = \
{
  "version": 1,
  "features": [
    {
      "name": "ApplicationHostname",
      "description": "Application Hostname strategy",
      "enabled": True,
      "strategies": [
        {
          "name": "applicationHostname",
          "parameters": {
            "hostNames": "iMacPro.local,test1,test2"
          }
        }
      ],
      "createdAt": "2018-10-09T06:05:14.757Z"
    },
    {
      "name": "Default",
      "description": "Default feature toggle",
      "enabled": True,
      "strategies": [
        {
          "name": "default",
          "parameters": {}
        }
      ],
      "createdAt": "2018-10-09T06:04:05.667Z"
    },
    {
      "name": "GradualRolloutRandom",
      "description": "Gradual Rollout Random example",
      "enabled": True,
      "strategies": [
        {
          "name": "gradualRolloutRandom",
          "parameters": {
            "percentage": 50
          }
        }
      ],
      "createdAt": "2018-10-09T06:05:37.637Z"
    },
    {
      "name": "GradualRolloutSessionId",
      "description": "SessionID check!",
      "enabled": True,
      "strategies": [
        {
          "name": "gradualRolloutSessionId",
          "parameters": {
            "percentage": 50,
            "groupId": "GradualRolloutSessionId"
          }
        }
      ],
      "createdAt": "2018-10-09T06:06:51.057Z"
    },
    {
      "name": "GradualRolloutUserID",
      "description": "GradualRolloutUserID strategy",
      "enabled": True,
      "strategies": [
        {
          "name": "gradualRolloutUserId",
          "parameters": {
            "percentage": 50,
            "groupId": "GradualRolloutUserID"
          }
        }
      ],
      "createdAt": "2018-10-09T06:07:17.520Z"
    },
    {
      "name": "RemoteAddress",
      "description": "RemoteAddress strategies",
      "enabled": True,
      "strategies": [
        {
          "name": "remoteAddress",
          "parameters": {
            "IPs": "69.208.0.0/29,70.208.1.1,2001:db8:1234::/48,2002:db8:1234:0000:0000:0000:0000:0001"
          }
        }
      ],
      "createdAt": "2018-10-09T06:08:42.398Z"
    },
    {
      "name": "UserWithId",
      "description": "UserWithId strategies",
      "enabled": True,
      "strategies": [
        {
          "name": "userWithId",
          "parameters": {
            "userIds": "meep@meep.com,test@test.com,wat@wat.com"
          }
        }
      ],
      "createdAt": "2018-10-09T06:09:19.203Z"
    },
    {
      "name": "ivantest",
      "description": "ivantest",
      "enabled": True,
      "strategies": [
        {
          "name": "flexibleRollout",
          "parameters": {
            "rollout": "21",
            "stickiness": "userId",
            "groupId": "ivantest"
          },
          "constraints": [
            {
              "contextName": "environment",
              "operator": "IN",
              "values": [
                "staging",
                "prod"
              ]
            },
            {
              "contextName": "userId",
              "operator": "NOT_IN",
              "values": [
                "1",
                "2",
                "3"
              ]
            },
            {
              "contextName": "userId",
              "operator": "IN",
              "values": [
                "4",
                "5",
                "6"
              ]
            },
            {
              "contextName": "appName",
              "operator": "IN",
              "values": [
                "test"
              ]
            }
          ]
        }
      ],
      "variants": None,
      "createdAt": "2019-10-05T07:30:29.896Z"
    }
  ]
}
