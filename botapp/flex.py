from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

def flex_example():
    #將JSON設定為變數content，並以FlexSendMessage()包成Flex Message
    content = {   "type": "carousel",
                  "contents": [
                    {
                      "type": "bubble",
                      "size": "nano",
                      "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "In Progress",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center"
                          },
                          {
                            "type": "text",
                            "text": "70%",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "filler"
                                  }
                                ],
                                "width": "70%",
                                "backgroundColor": "#0D8186",
                                "height": "6px"
                              }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                          }
                        ],
                        "backgroundColor": "#27ACB2",
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px"
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "Buy milk and lettuce before class",
                                "color": "#8C8C8C",
                                "size": "sm",
                                "wrap": True
                              }
                            ],
                            "flex": 1
                          }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                      },
                      "styles": {
                        "footer": {
                          "separator": False
                        }
                      }
                    },
                    {
                      "type": "bubble",
                      "size": "nano",
                      "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Pending",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center"
                          },
                          {
                            "type": "text",
                            "text": "30%",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "filler"
                                  }
                                ],
                                "width": "30%",
                                "backgroundColor": "#DE5658",
                                "height": "6px"
                              }
                            ],
                            "backgroundColor": "#FAD2A76E",
                            "height": "6px",
                            "margin": "sm"
                          }
                        ],
                        "backgroundColor": "#FF6B6E",
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px"
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "Wash my car",
                                "color": "#8C8C8C",
                                "size": "sm",
                                "wrap": True
                              }
                            ],
                            "flex": 1
                          }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                      },
                      "styles": {
                        "footer": {
                          "separator": False
                        }
                      }
                    }
                  ]
                }
    message=FlexSendMessage(alt_text='FlexMessage範例',contents=content)
    return message