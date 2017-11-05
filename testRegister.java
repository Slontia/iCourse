package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class TestRegister {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "http://127.0.0.1:8000/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testRegister() throws Exception {
    driver.get(baseUrl + "/");
    driver.findElement(By.cssSelector("button.el-button.el-button--text")).click();
    driver.findElement(By.xpath("//body/ul/li[2]")).click();
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fkd");
    driver.findElement(By.cssSelector("#register_form2 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form2 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("方科栋");
    driver.findElement(By.cssSelector("div.el-select > div.el-input > input.el-input__inner")).click();
    driver.findElement(By.cssSelector("li.el-select-dropdown__item.hover")).click();
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456");
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).click();
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456");
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("fang");
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("fangkedong@buaa.edu.cn");
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456789");
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456789");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("用户名或邮箱已被注册", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fkdfkd");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("用户名或邮箱已被注册", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fangkedong@10.2.28.124");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fkd15061188");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer")).click();
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("用户名或邮箱已被注册", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("15061188@buaa.edu.cn");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("注册成功", closeAlertAndGetItsText());
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
