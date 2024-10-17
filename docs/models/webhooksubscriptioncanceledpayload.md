# WebhookSubscriptionCanceledPayload

Sent when a subscription is canceled by the user.
They might still have access until the end of the current period.

**Discord & Slack support:** Full


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `data`                                                                                               | [models.SubscriptionInput](../models/subscriptioninput.md)                                           | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `type`                                                                                               | [models.WebhookSubscriptionCanceledPayloadType](../models/webhooksubscriptioncanceledpayloadtype.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |