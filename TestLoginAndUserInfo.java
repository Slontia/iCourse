package seleniumDemo.Desktop;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class TestLoginAndUserInfo {
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
  public void testLoginLogout() throws Exception {
    driver.get("http://127.0.0.1:8000/course");
    driver.findElement(By.cssSelector("button.el-button.el-button--text")).click();
    driver.findElement(By.cssSelector("li.el-dropdown-menu__item")).click();
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fkd15061188");
    driver.findElement(By.cssSelector("div.el-input.el-input--small > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("div.el-input.el-input--small > input.el-input__inner")).sendKeys("123456789");
    driver.findElement(By.cssSelector("button.el-button.el-button--primary")).click();
    assertEquals("登录成功", closeAlertAndGetItsText());
    WebDriverWait wait = new WebDriverWait(driver, 20);
    wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("button.el-button.el-button--text")));
    WebElement element = driver.findElement(By.cssSelector("button.el-button.el-button--text"));
    ((JavascriptExecutor)driver).executeScript("arguments[0].click();", element);
    
    wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("li.el-dropdown-menu__item")));
    element = driver.findElement(By.cssSelector("li.el-dropdown-menu__item"));
    ((JavascriptExecutor)driver).executeScript("arguments[0].click();", element);
    driver.findElement(By.cssSelector("li.el-menu-item")).click();
    driver.findElement(By.xpath("//div[@id='personal']/div[2]/ul/li[2]")).click();
    assertEquals("还未开放", closeAlertAndGetItsText());
    driver.findElement(By.xpath("//div[@id='personal']/div[2]/ul/li[3]")).click();
    assertEquals("还未开放", closeAlertAndGetItsText());
    driver.findElement(By.xpath("//div[@id='personal']/div[2]/ul/li[4]")).click();
    assertEquals("还未开放", closeAlertAndGetItsText());
    driver.findElement(By.xpath("//div[@id='personal']/div[2]/ul/li[5]")).click();
    assertEquals("还未开放", closeAlertAndGetItsText());
  }

  @After
  public void tearDown() throws Exception {
    
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
