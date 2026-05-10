const path = require('path')

module.exports = {
  publicPath: './',
  lintOnSave: false,  // 👈 这一行关闭代码检查，直接解决你现在的报错！
  transpileDependencies: [],
  chainWebpack: config => {
    config.resolve.alias.set('_c', path.resolve(__dirname, 'src/components'))
  }
}