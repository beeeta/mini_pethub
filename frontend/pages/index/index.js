//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    pageData: [
      {
        "id": 1,
        "imgUrl": "1_imgurl",
        "detailUrl": "1_detailUrl"
      },
      {
        "id": 2,
        "imgUrl": "2_imgurl",
        "detailUrl": "2_detailUrl"
      },
      {
        "id": 3,
        "imgUrl": "3_imgurl",
        "detailUrl": "3_detailUrl"
      },
      {
        "id": 4,
        "imgUrl": "4_imgurl",
        "detailUrl": "4_detailUrl"
      },
      {
        "id": 5,
        "imgUrl": "5_imgurl",
        "detailUrl": "5_detailUrl"
      }
    ]
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    var appobj = this;
    wx.getUserInfo({
      success:function(e){
        app.globalData.userInfo = e.userInfo
        appobj.setData({
          userInfo: e.userInfo,
          hasUserInfo: true
        })
      }
    });

  },
  showDetail: function (e) {
    wx.navigateTo({
      url: "/pages/item/item?id="+e.currentTarget.dataset.id
    })
  },
  testit:function(){
    console.log(this.data.userInfo)
  }
})
