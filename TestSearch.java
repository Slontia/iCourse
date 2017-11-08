package seleniumDemo.Desktop;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class TestSearch {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
	  System.setProperty("webdriver.gecko.driver", "C:\\Users\\15061188\\Downloads\\geckodriver-v0.19.0-win32\\geckodriver.exe");
    driver = new FirefoxDriver();
    baseUrl = "http://10.2.28.124:8000/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testSearch() throws Exception {
    driver.get("http://127.0.0.1:8000/course");
    driver.findElement(By.xpath("//div[@id='header']/div/div/div[2]/ul/li[2]")).click();
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("论语");
    driver.findElement(By.cssSelector("div.el-form-item__content > button.el-button.el-button--primary")).click();
    assertEquals("成功！开始搜索", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("语");
    driver.findElement(By.cssSelector("div.el-form-item__content > button.el-button.el-button--primary")).click();
    assertEquals("成功！开始搜索", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("软件");
    driver.findElement(By.cssSelector("div.el-form-item__content > button.el-button.el-button--primary")).click();
    assertEquals("成功！开始搜索", closeAlertAndGetItsText());
    driver.findElement(By.xpath("//div[@id='course']/div[2]/section/div/div/div/section/div[2]/div/div[2]/table/thead/tr/th[2]/div")).click();
    driver.findElement(By.xpath("//div[@id='course']/div[2]/section/div/div/div/section/div[2]/div/div[2]/table/thead/tr/th[3]/div")).click();
    driver.findElement(By.xpath("//div[@id='course']/div[2]/section/div/div/div/section/div[2]/div/div[2]/table/thead/tr/th[4]/div")).click();
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("公共");
    driver.findElement(By.cssSelector("div.el-form-item__content > button.el-button.el-button--primary")).click();
    assertEquals("成功！开始搜索", closeAlertAndGetItsText());
    driver.findElement(By.xpath("//div[@id='course']/div[2]/section/div/div/div/section/div[2]/div/div[2]/table/thead/tr/th[2]/div")).click();
    driver.findElement(By.xpath("//div[@id='course']/div[2]/section/div/div/div/section/div[2]/div/div[2]/table/thead/tr/th[3]/div")).click();
    driver.findElement(By.xpath("//div[@id='course']/div[2]/section/div/div/div/section/div[2]/div/div[2]/table/thead/tr/th[4]/div")).click();
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
	  WebDriverWait wait = new WebDriverWait(driver, 10);
	  Alert alert=null;
      try {
           alert= wait.until(new ExpectedCondition<Alert>() {
              @Override
              public Alert apply(WebDriver driver) {
                  try {
                      return driver.switchTo().alert();
                  } catch (NoAlertPresentException e) {
                      return null;
                  }
              }
          });
          String alertText = alert.getText();
          if (acceptNextAlert) {
            alert.accept();
          } else {
            alert.dismiss();
          }
          return alertText;
      } catch (NullPointerException e) {
      } finally {
          acceptNextAlert = true;   
      }
      return alert.getText();
  }
}
